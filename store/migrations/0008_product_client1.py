# Generated by Django 3.2 on 2022-10-03 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_category_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='client1',
            field=models.TextField(null=True),
        ),
    ]