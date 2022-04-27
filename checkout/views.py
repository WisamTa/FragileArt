from django.shortcuts import render

from store.models import Product

# Create your views here.

def checkout(request):
    """A View to return the checkout form"""
    return render(request, 'checkout/checkout.html')