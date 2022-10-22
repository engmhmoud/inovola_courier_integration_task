
from django.dispatch import receiver
from django.db.models.signals import pre_save
from base.models.base import Order
from integration.integrate import create_order


@receiver(pre_save, Order)
def create_order_signal(sender, instance, **kwargs):
    created = kwargs.get("created", instance._state.adding)
    if created:
        create_order()
