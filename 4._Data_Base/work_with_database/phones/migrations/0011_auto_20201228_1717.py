# Generated by Django 2.2 on 2020-12-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0010_auto_20201228_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
