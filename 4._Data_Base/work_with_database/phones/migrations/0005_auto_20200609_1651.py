# Generated by Django 2.2.10 on 2020-06-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0004_auto_20200608_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=7),
        ),
    ]
