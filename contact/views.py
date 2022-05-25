from django.shortcuts import render


def contact(request):
    """A View to return index page"""
    return render(request, 'contact/contact.html')
