# Generated by Django 3.2.18 on 2023-09-04 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appPedidos', '0013_alter_shippingaddress_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appPedidos.usuario_model'),
        ),
    ]