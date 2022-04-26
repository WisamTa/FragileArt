from django.shortcuts import render

# Create your views here.

def portfolio(request):
    """A View to return index page"""
    return render(request, 'portfolio/portfolio.html')