# Generated by Django 4.1.7 on 2023-02-24 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almendra_app', '0022_alter_pasteleria_model_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasteleria_model',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]
