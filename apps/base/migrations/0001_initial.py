# Generated by Django 5.0.1 on 2024-02-24 08:57

import django.db.models.deletion
import django_resized.forms
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='places/', verbose_name='фото с мест на которых бывали')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок для фотографии')),
                ('photo', models.ImageField(upload_to='details/', verbose_name='фото для деталей')),
                ('description', models.TextField(verbose_name='Описание для фото')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Дата создания новости')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='logo/', verbose_name='Логотип')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок для фотографии')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='logo/', verbose_name='Картинка')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Почта')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
            ],
            options={
                'verbose_name': 'Настройки сайта',
                'verbose_name_plural': 'Настройки сайта ',
            },
        ),
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='homepage/widget')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Ссылка на Фейсбук')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Ссылка на Твиттер')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Ссылка на Инсту')),
                ('yotube', models.URLField(blank=True, max_length=255, null=True, verbose_name='Ссылка на ютуб')),
            ],
            options={
                'verbose_name': 'Виджет',
                'verbose_name_plural': 'Виджеты',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок новости')),
                ('descriptions', models.TextField(verbose_name='Описание новости')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='image/')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Дата создания новости')),
                ('comments', models.ManyToManyField(blank=True, related_name='news_comments', to='base.review')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
