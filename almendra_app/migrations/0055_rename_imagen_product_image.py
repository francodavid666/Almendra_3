# Generated by Django 3.2.18 on 2023-09-04 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almendra_app', '0054_rename_image_product_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='imagen',
            new_name='image',
        ),
    ]
