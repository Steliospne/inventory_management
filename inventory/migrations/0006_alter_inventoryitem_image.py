# Generated by Django 4.2.6 on 2023-10-16 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_inventoryitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='image',
            field=models.ImageField(default='', upload_to='items_img'),
        ),
    ]
