from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('line_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'order_date', 'delivery_charge', 'total_order', 'grand_total',)

    list_display = ('order_number', 'order_date', 'first_name', 'last_name', 
                    'delivery_charge', 'total_order', 'grand_total',)

    ordering = ('-order_date',)

admin.site.register(Order, OrderAdmin)
