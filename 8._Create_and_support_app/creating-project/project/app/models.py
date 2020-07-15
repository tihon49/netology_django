from django.db import models



class Station(models.Model):
    name = models.CharField('Имя', max_length=100)
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')
    routes = models.ManyToManyField('Route', related_name = "stations", verbose_name='Номер маршрута')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Остановка'
        verbose_name_plural = 'Остановки'



class Route(models.Model):
    name = models.CharField('Номер маршрута', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Номер маршрута'
        verbose_name_plural = 'Номера маршрутов'