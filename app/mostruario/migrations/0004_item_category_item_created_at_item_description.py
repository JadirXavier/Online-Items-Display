# Generated by Django 5.0.8 on 2024-08-20 15:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mostruario", "0003_remove_item_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="category",
            field=models.CharField(
                choices=[
                    ("Artesanato", "Artesanato"),
                    ("Roupas", "Roupas"),
                    ("Bolsas", "Bolsas"),
                ],
                default="Roupas",
                max_length=50,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="item",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="item",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
