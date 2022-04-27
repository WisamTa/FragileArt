from store.models import Product
from django.shortcuts import render, get_object_or_404


def portfolio(request):
    """A View to display all saleable items"""

    portfolio = Product.objects.all()

    context = {
        'portfolio': portfolio,
    }

    return render(request, 'portfolio/portfolio.html', context)


def portfolio_detail(request, product_id):
    """A View to display and individual product detail"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'portfolio/portfolio-detail.html', context)
