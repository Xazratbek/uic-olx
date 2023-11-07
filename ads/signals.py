from django.db.models.signals import pre_save
from django.dispatch import receiver
from ads.models import Ads


@receiver(pre_save, sender=Ads)
def update_detail(sender, instance, *args, **kwargs):
    instance.address = instance.get_address_text()
