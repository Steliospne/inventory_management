# Generated by Django 4.2.6 on 2023-10-16 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_inventoryitem_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='items_img'),
        ),
    ]