from django.contrib import admin
from .models import Client

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'business_type',
        'description',
        'image',
    )

admin.site.register(Client, ClientAdmin)
