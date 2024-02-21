from django.db import models
from django_resized.forms import ResizedImageField
from django.contrib.auth.models import User


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
    photo = models.ImageField(
        upload_to='logo/',
        verbose_name='Картинка'
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
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта "


class Blogpost(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='places/',
        verbose_name="фото с мест на которых бывали",

    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Заголовок для фотографии'
    )
    photo = models.ImageField(
        upload_to='details/',
        verbose_name='фото для деталей',
    )
    description = models.TextField(
        verbose_name = 'Описание для фото'
    )
    create = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания новости"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Widget(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Заголовок'
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
    image = models.ImageField(
        upload_to='homepage/widget'
    )
    
    facebook = models.URLField(
        verbose_name='Ссылка на Фейсбук',
        blank=True, null=True
    )
    twitter = models.URLField(
        verbose_name='Ссылка на Твиттер',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Ссылка на Инсту',
        blank=True, null=True
    )
    yotube = models.URLField(
        max_length=255,
        verbose_name='Ссылка на ютуб',
        blank=True, null=True
    )

    def __str__ (self):
        return self.title
    class Meta:
        verbose_name = 'Виджет'
        verbose_name_plural = 'Виджеты'



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
    create_date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания новости"
    )
    comments = models.ManyToManyField('Review', related_name='news_comments', blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class Review(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    comment = models.CharField(
        max_length=255,
        verbose_name='Комментарий',
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.user.username