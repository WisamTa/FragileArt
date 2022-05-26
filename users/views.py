from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import ProfileForm
from checkout.models import Order


# Create your views here.

def user(request):
    """A View to display a users profile"""
    
    # user = get_object_or_404(UserProfile, user=request.user)
    # form = ProfileForm(instance=user)
    # orders = user.orders.all()

    template = 'users/user.html'
    # context = {
    #     'form': form,
    #     'orders': orders,
    # }
    context = {}

    return render(request, template, context)

def order_history(request, order_number):
    """ retrieves the users order history """
    order = get_object_or_404(Order, order_number=order_number)
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)