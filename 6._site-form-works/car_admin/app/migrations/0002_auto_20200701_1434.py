# Generated by Django 2.2.7 on 2020-07-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Машина', 'verbose_name_plural': 'Машины'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Обзор', 'verbose_name_plural': 'Обзоры'},
        ),
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]