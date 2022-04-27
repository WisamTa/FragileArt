from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs)
    """
    To Update the order total on line update/Create
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def delete_on_save(sender, instance, **kwargs):
    """
    To Update the order total on line deleted
    """
    instance.order.update_total()