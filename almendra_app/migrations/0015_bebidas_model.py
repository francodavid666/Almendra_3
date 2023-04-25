# Generated by Django 4.1 on 2023-02-19 02:13

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almendra_app', '0014_remove_pasteleria_model_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='bebidas_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('titulo', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('precio', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
