# Generated by Django 4.1.7 on 2023-05-31 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='flight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='passenger', to='dashboard.flight'),
        ),
    ]