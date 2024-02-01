from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

# Update order total on lineitem update/create
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    print('sender', sender)
    print('instance', instance)
    print('created', created)
    instance.order.update_total()

# Update order total on lineitem delete
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()