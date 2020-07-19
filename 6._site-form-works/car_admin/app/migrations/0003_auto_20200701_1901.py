# Generated by Django 2.2.10 on 2020-07-01 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200701_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=50, verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=50, verbose_name='Модедь'),
        ),
        migrations.AlterField(
            model_name='review',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Car', verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(verbose_name='Текст обзора'),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='Заголовок'),
        ),
    ]