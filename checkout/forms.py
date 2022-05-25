from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order 
        fields = ('first_name', 'last_name', 'email', 'telephone_number', 
                'street_address1', 'street_address2', 'city_town', 'county_state', 
                'postcode_zip', 'country',)

    def __init__(self, *args, **kwargs):
        """
        Placeholders and class to remove auto gen labels and to autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'E-mail Address',
            'telephone_number': 'Telephone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'city_town': 'City Or Town',
            'county_state': 'County Or State',
            'postcode_zip': 'Postcode or Zipcode',
            'country': 'Country',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = f'{placeholders[field]}'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
