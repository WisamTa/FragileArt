from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

def clients(request):
    """A View to return index page"""
    return render(request, 'clients/clients.html')