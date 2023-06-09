# Generated by Django 3.2.18 on 2023-06-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almendra_app', '0048_alter_bebidas_model_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='desayunos_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='desayunos/')),
                ('titulo', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=70, null=True)),
                ('informacion', models.CharField(blank=True, max_length=184, null=True)),
                ('precio', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
