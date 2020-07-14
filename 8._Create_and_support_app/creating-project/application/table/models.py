import os
from django.db import models



class Table(models.Model):
    '''Класс описания колонок таблицы'''
    name = models.CharField('Имя', max_length=100)
    width = models.PositiveIntegerField('Ширина')
    number = models.PositiveIntegerField('Порядковый номер')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Колонка'
        verbose_name_plural = 'Колонки'



class CSVFile(models.Model):
    '''Класс пути к CSV файлу'''
    dir_path = os.getcwd()
    path = models.FilePathField('Путь к файлу', path=dir_path, match='“*\.csv$', recursive=True, max_length=1000)

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        self.save()

    def __str__(self):
        return self.path

    class Meta:
        verbose_name = 'Путь к файлу'
        verbose_name_plural = 'Путь к файлу'