# Generated by Django 2.2.10 on 2020-07-23 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_summerwear_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='description',
            field=models.CharField(blank=True, max_length=250, verbose_name='Краткое описание'),
        ),
    ]
