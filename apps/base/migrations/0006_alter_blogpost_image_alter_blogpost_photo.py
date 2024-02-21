# Generated by Django 5.0.2 on 2024-02-21 18:24

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_blogpost_widget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='places/', verbose_name='фото с мест на которых бывали'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='details/', verbose_name='фото для деталей'),
        ),
    ]
