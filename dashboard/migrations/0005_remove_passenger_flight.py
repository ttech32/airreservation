# Generated by Django 4.1.7 on 2023-06-19 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_passenger_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='flight',
        ),
    ]