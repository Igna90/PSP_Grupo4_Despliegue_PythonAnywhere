# Generated by Django 3.1.2 on 2022-01-24 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0008_auto_20220124_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='assets/img/', verbose_name='Imagen'),
        ),
    ]
