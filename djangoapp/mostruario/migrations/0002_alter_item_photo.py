# Generated by Django 5.0.8 on 2024-08-16 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mostruario", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="items/"),
        ),
    ]
