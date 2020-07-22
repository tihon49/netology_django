from django.db import models



class Phone(models.Model):
    name = models.CharField('Название', max_length=250)
    price = models.DecimalField('Цена', max_digits=20, decimal_places=2)
    image = models.ImageField('Изображение')

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
        ordering = ['price']

    def __str__(self):
        return self.name



class SummerWear(models.Model):
    name = models.CharField('Название', max_length=250)
    price = models.DecimalField('Цена', max_digits=20, decimal_places=2)
    image = models.ImageField('Изображение')

    class Meta:
        verbose_name = 'К лету'
        verbose_name_plural = 'К лету'
        ordering = ['price']

    def __str__(self):
        return self.name