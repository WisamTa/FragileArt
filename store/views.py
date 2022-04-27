from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def store(request):
    """A View to display all saleable items"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'store/store.html', context)

    
def item_detail(request, product_id):
    """A View to display and individual product detail"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'store/item-detail.html', context)