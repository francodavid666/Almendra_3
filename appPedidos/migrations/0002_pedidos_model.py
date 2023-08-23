# Generated by Django 3.2.18 on 2023-08-14 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPedidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pedidos_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('tamanio', models.CharField(blank=True, max_length=30, null=True)),
                ('azucar', models.CharField(blank=True, max_length=30, null=True)),
                ('adicional', models.CharField(blank=True, max_length=30, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
