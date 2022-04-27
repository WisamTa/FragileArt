from django.shortcuts import render
from .models import Client


def clients(request):
    """A View to return index page"""

    clients = Client.objects.all()

    context = {
        'clients': clients,
    }

    return render(request, 'clients/clients.html', context)
