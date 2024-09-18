from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import ItemPhoto
import cloudinary.uploader

@receiver(post_delete, sender=ItemPhoto)
def delete_photo_file(sender, instance, **kwargs):
    if instance.photo:
        # Deleta a imagem do Cloudinary
        cloudinary.uploader.destroy(instance.photo.public_id)