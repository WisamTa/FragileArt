from django.shortcuts import render

# Create your views here.

def contact(request):
    """A View to return index page"""
    return render(request, 'contact/contact.html')