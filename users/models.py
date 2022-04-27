from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class UserProfile(models.Model):
    """
    A Model for the user profile for storing default information and order history
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32, null=False, blank=False)
    last_name = models.CharField(max_length=64, null=False, blank=False)
    email = models.EmailField(max_length=256, null=False, blank=False)
    default_telephone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=128, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=128, null=True, blank=True)
    default_city_town = models.CharField(max_length=128, null=True, blank=True)
    default_county_state = models.CharField(max_length=64, null=True, blank=True)
    default_postcode_zip = models.CharField(max_length=12, null=True, blank=True)
    default_country = CountryField(blank_label='Country*', null=True, blank=True)

    def __str__(self):
        return self.user.username

