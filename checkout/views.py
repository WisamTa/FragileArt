from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required

import stripe
import sweetify

from store.models import Product
from .forms import OrderForm
from users.forms import UserProfile

from .models import Order, OrderLineItem

@login_required(login_url="/accounts/login")
def checkout(request):
    """A View to return the checkout form"""

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'telephone_number': request.POST['telephone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'city_town': request.POST['city_town'],
            'county_state': request.POST['county_state'],
            'postcode_zip': request.POST['postcode_zip'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, quantity in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    sweetify.error(request, title='Ooops', text='One of the products in your basket wasn\'t found!',
                 icon='error')
                    order.delete()
                    return redirect(reverse('view_basket'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            sweetify.error(request, title='Ooops', text='There has been a problem with your submission',
                 icon='error')
            return redirect(reverse('store'))
    else:
        basket = request.session.get('basket', {})
        if not basket:
            sweetify.error(request, title='Ooops', text='Errrrr there is nothing in here!',
                 icon='error')
            return redirect(reverse('store'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        
        #Stripe
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )
        order_form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key, 
            'client_secret': intent.client_secret,
        }
        return render(request, template, context)

def checkout_success(request, order_number):
    """
    A view to handle successful checkout
    """

    request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    user = UserProfile.objects.get(user=request.user)
    order.user_profile = user
    order.save()


    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout-success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

