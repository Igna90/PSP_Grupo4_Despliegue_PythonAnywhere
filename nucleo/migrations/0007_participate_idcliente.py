# Generated by Django 3.1.2 on 2022-01-22 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0006_auto_20220121_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='participate',
            name='idCliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id'),
        ),
    ]
