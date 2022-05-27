# Generated by Django 3.2 on 2022-05-27 14:29

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=256)),
                ('telephone_number', models.CharField(max_length=20)),
                ('street_address1', models.CharField(max_length=128)),
                ('street_address2', models.CharField(blank=True, max_length=128, null=True)),
                ('city_town', models.CharField(max_length=128)),
                ('county_state', models.CharField(blank=True, max_length=64, null=True)),
                ('postcode_zip', models.CharField(max_length=12)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total_order', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('delivery_charge', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='users.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('line_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
