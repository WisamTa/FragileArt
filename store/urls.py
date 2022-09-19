from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<product_id>', views.item_detail, name='item_detail'),

]