# Generated by Django 2.2.10 on 2020-07-29 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20200729_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_items_count',
            field=models.IntegerField(default=0, verbose_name='Общее количество товаров в заказе'),
        ),
    ]
