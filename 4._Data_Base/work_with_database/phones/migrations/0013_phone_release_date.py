# Generated by Django 2.2 on 2020-12-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0012_remove_phone_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
