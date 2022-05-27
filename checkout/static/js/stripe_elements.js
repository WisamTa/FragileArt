let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
let card = elements.create('card', {
    style: style
});
card.mount('#card-element');


card.addEventListener('change', function (event) {
    let errorCont = document.getElementById('card-errors');
    if (event.error) {
        let html = `<span><p class="text-danger">${event.error.message}</span>`
        $(errorCont).html(html)

    } else {
        errorCont.textContent = ''
    }
})

// Form submission

let form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({
        'disabled': true
    })
    $('#submit-button').attr('disabled', true)
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: 'Jenny Rosen'
            }
        }
    }).then(function (result) {
        if (result.error) {
            let errorCont = document.getElementById('card-errors');
            let html = `<span><p class="text-danger">${result.error.message}</span>`;
            $(errorCont).html(html);
            card.update({
                'disabled': false
            })
            $('#submit-button').attr('disabled', false)
        } else {
            // The payment has been processed!
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
