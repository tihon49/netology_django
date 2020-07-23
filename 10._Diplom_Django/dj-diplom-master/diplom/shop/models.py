from django.contrib.auth.models import User
from django.db import models



class Phone(models.Model):
    '''Модель телефона'''
    name = models.CharField('Название', max_length=250)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    description = models.CharField('Краткое описание', max_length=250, blank=True)
    price = models.DecimalField('Цена', max_digits=20, decimal_places=2)
    image = models.ImageField('Изображение')

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
        ordering = ['price']

    def __str__(self):
        return self.name



class SummerWear(models.Model):
    '''Модель летней одежды'''
    name = models.CharField('Название', max_length=250)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    description = models.CharField('Краткое описание', max_length=250, blank=True)
    price = models.DecimalField('Цена', max_digits=20, decimal_places=2)
    image = models.ImageField('Изображение')

    class Meta:
        verbose_name = 'К лету'
        verbose_name_plural = 'К лету'
        ordering = ['price']

    def __str__(self):
        return self.name



class Review(models.Model):
    phone = models.ForeignKey(Phone, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=250)
    text = models.TextField('Отзыв')
    star = models.IntegerField(null=True, blank=True)
    session_id = models.CharField('id сессии', max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-id']