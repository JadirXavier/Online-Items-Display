from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import ItemPhoto

@receiver(post_delete, sender=ItemPhoto)
def delete_photo_file(sender, instance, **kwargs):
    if instance.photo:
        instance.photo.delete(save=False)