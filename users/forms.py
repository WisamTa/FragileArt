from django import forms
from .models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        """
        Placeholders for classes and remove auto-generation
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_telephone_number': 'Phone Number',
            'default_street_address1 ': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_city_town': 'Town or City',
            'default_county_state': 'County or State',
            'default_postcode_zip': 'Postal Code',
        }