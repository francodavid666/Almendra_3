# Generated by Django 4.1.7 on 2023-03-20 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almendra_app', '0034_alter_bebidas_model_informacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasteleria_model',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
