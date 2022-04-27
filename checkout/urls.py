from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success')

]