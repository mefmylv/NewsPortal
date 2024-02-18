from django.db import models
from django_resized.forms import ResizedImageField

# Create your models here.
class Settings(models.Model):
    logo = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo/',
        verbose_name="Логотип",
        blank = True, null = True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок для фотографии"
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Номер телефона'
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Почта',
        blank=True, null=True
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Facebook',
        blank=True, null=True
    )
    twitter = models.URLField(
        verbose_name='Twitter',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Instagram',
        blank=True, null=True
    )
    telegram = models.URLField(
        max_length=255,
        verbose_name='Telegram',
        blank=True, null=True
    )

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта "



class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок новости"
    )
    descriptions = models.TextField(
        verbose_name="Описание новости"
    )
    image = ResizedImageField(
        force_format="WEBP",
	    quality=100,
        upload_to="image/"
    )
    create = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания новости",
        blank=True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"