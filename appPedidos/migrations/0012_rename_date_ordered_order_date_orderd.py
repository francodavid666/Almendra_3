# Generated by Django 3.2.18 on 2023-09-02 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appPedidos', '0011_auto_20230902_0156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_ordered',
            new_name='date_orderd',
        ),
    ]