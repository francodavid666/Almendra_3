# Generated by Django 4.1.7 on 2023-03-22 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almendra_app', '0035_alter_pasteleria_model_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='login_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('constraseña', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
