# Generated by Django 4.1.7 on 2023-03-12 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almendra_app', '0033_alter_brunch_model_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bebidas_model',
            name='informacion',
            field=models.CharField(blank=True, max_length=184, null=True),
        ),
        migrations.AlterField(
            model_name='populares_model',
            name='informacion',
            field=models.CharField(blank=True, max_length=184, null=True),
        ),
        migrations.AlterField(
            model_name='salados_model',
            name='informacion',
            field=models.CharField(blank=True, max_length=184, null=True),
        ),
    ]
