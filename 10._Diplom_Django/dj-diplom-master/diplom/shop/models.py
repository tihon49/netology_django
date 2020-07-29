from django.contrib.auth.models import User
from django.db import models



class Item(models.Model):
    '''Модель товара'''
    name = models.CharField('Название', max_length=250)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    category = models.ForeignKey('Category', verbose_name='Категория товара', on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField('Краткое описание', max_length=250, blank=True)
    price = models.DecimalField('Цена', max_digits=20, decimal_places=2)
    image = models.ImageField('Изображение')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['price']

    def __str__(self):
        return self.name



class Category(models.Model):
    '''Класс категории товара'''
    name = models.CharField('Название категории', max_length=250)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name



class Review(models.Model):
    '''Модель отзыва к товару'''
    item = models.ForeignKey(Item, related_name='reviews', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField('Имя', max_length=250)
    text = models.TextField('Отзыв')
    star = models.IntegerField(null=True, blank=True)
    session_id = models.CharField('id сессии', max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-id']