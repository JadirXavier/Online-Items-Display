from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    CATEGORIES = [
        ('Artesanato', 'Artesanato'),
        ('Roupas', 'Roupas'),
        ('Bolsas', 'Bolsas'),
    ]
    name = models.CharField(max_length=100, verbose_name="Nome")
    photo = models.ImageField(upload_to='items/', blank=True, null=True, verbose_name="Foto")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    category = models.CharField(max_length=50, choices=CATEGORIES, verbose_name="Categoria")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Criado por")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    def __str__(self):
        return self.name