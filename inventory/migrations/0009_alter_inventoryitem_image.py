# Generated by Django 4.2.6 on 2023-10-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_inventoryitem_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryitem',
            name='image'
        )
        
    ]
