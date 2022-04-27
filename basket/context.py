from decimal import Decimal
from django.conf import settings
from store.models import Product
from django.shortcuts import get_object_or_404



def basket_contents(request):

    basket_items = []
    total = 0
    item_count = 0
    
    

    basket = request.session.get('basket', {})
    

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        item_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })
    delivery = total * Decimal(settings.DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context