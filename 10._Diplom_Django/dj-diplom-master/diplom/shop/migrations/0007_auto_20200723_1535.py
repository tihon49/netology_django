# Generated by Django 2.2.10 on 2020-07-23 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_phone_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Имя')),
                ('text', models.TextField(verbose_name='Отзыв')),
                ('stars', models.IntegerField()),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='shop.Phone')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
