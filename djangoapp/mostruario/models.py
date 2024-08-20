from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    CATEGORIES = [
        ('Artesanato', 'Artesanato'),
        ('Roupas', 'Roupas'),
        ('Bolsas', 'Bolsas'),
    ]
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='items/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name