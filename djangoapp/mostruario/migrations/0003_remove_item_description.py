# Generated by Django 5.1 on 2024-08-19 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mostruario', '0002_alter_item_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
    ]
