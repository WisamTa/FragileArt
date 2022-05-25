from django.db import models
from django.db.models import Sum
from django.conf import settings 

from store.models import Product
from users.models import UserProfile


from django_countries.fields import CountryField
import uuid


class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    first_name = models.CharField(max_length=32, null=False, blank=False)
    last_name = models.CharField(max_length=64, null=False, blank=False)
    email = models.EmailField(max_length=256, null=False, blank=False)
    telephone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=128, null=False, blank=False)
    street_address2 = models.CharField(max_length=128, null=True, blank=True)
    city_town = models.CharField(max_length=128, null=False, blank=False)
    county_state = models.CharField(max_length=64, null=True, blank=True)
    postcode_zip = models.CharField(max_length=12, null=False, blank=False)
    country = CountryField(blank_label='Country*', null=False, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    total_order = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    delivery_charge = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)


    def _order_number_generation(self):
        """
        Generates a random order number ( Private method )
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        If the order number has not been set, override the original save method to set the order number
        """
        if not self.order_number:
            self.order_number = self._order_number_generation()
        super().save(*args, **kwargs)
    
    def total_update(self):
        """
        Updates the grand total as a new line is added and accounts for delivery cost to suit
        """
        self.total_order = self.lineitems.aggregate(Sum('line_total'))['line_total__sum'] or 0
        self.delivery_charge = self.total_order * settings.DELIVERY_PERCENTAGE / 100
        self.grand_total = self.total_order + self.delivery_charge
        self.save()

    def __str__(self):
        return self.order_number
        

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    line_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        To Override the save method to set the line_total and update order total 
        """
        self.line_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Name:{self.product.name} on order {self.order.order_number}'
