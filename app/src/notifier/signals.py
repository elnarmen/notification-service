from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Client


@receiver(pre_save, sender=Client)
def update_operator_code(sender, instance, **kwargs):
    # при создании или изменении объекта Client обновляем значение поля operator_code
    instance.operator_code = str(instance.phone_number)[1:4]
