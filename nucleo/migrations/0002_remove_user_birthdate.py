# Generated by Django 3.1.2 on 2022-01-14 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthDate',
        ),
    ]
