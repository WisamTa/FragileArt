from django.shortcuts import render
from django.db import models
from store.models import Product


# Create your views here.

def portfolio(request):
    """A View to display all saleable items"""

    portfolio = Product.objects.all()

    context = {
        'portfolio': portfolio,
    }

    return render(request, 'portfolio/portfolio.html', context)
