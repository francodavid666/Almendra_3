# Generated by Django 4.1.7 on 2023-03-27 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almendra_app', '0039_remove_brunch_model_p6'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brunch_model',
            name='descripcion',
        ),
    ]
