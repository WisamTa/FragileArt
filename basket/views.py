from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse

from store.models import Product

# Create your views here.

def basket(request):
    """A View to return the users basket"""
    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    """ Add the requested item to the basket"""

    item = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)

def update_basket(request, item_id):
    """ A View to update the basket with """

    item = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('basket'))

def delete_basket_item(request, item_id):
    """ A view to delete selected item from the session basket """

    item = get_object_or_404(Product, pk=item_id)
    basket = request.session.get('basket', {})
    basket.pop(item_id)

    # Messages to be added later

    request.session['basket'] = basket
    return redirect(reverse('basket'), HttpResponse(status=200))

    # error handling 
