# Generated by Django 5.0.1 on 2024-02-21 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_review_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Комментарий'),
        ),
    ]
