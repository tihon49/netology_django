# Generated by Django 2.2.10 on 2020-07-09 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerGameInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('try_count', models.IntegerField(default=0)),
                ('num', models.IntegerField(default=0)),
                ('master', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='game.Player')),
                ('players', models.ManyToManyField(related_name='games', to='game.Player')),
            ],
        ),
    ]
