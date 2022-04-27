from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<product_id>', views.portfolio_detail, name='portfolio_detail'),

]