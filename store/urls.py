from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<product_id>', views.item_detail, name='item_detail'),

]