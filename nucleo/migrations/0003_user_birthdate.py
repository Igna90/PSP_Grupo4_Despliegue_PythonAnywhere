# Generated by Django 3.1.2 on 2022-01-14 18:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0002_remove_user_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthDate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de cumpleaños'),
            preserve_default=False,
        ),
    ]
