from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Item(models.Model):
    CATEGORIES = [
        ('Amigurumi', 'Amigurumi'),
        ('Roupas', 'Roupas'),
        ('Bolsas', 'Bolsas'),
    ]
    name = models.CharField(max_length=100, verbose_name="Nome")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    category = models.CharField(max_length=50, choices=CATEGORIES, verbose_name="Categoria")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Criado por")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    def __str__(self):
        return self.name

class ItemPhoto(models.Model):
    item = models.ForeignKey(Item, related_name='photos', on_delete=models.CASCADE)
    photo = CloudinaryField(verbose_name="Foto")

    def __str__(self):
        return f"Photo for {self.item.name}"
