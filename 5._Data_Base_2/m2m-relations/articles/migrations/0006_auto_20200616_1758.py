# Generated by Django 2.2.10 on 2020-06-16 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20200615_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(verbose_name='Основной раздел')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование раздела')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
            },
        ),
        migrations.RemoveField(
            model_name='thematic_section',
            name='articles',
        ),
        migrations.DeleteModel(
            name='ArticleThematic',
        ),
        migrations.DeleteModel(
            name='Thematic_section',
        ),
        migrations.AddField(
            model_name='articlesection',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Section'),
        ),
        migrations.AddField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(through='articles.ArticleSection', to='articles.Section'),
        ),
    ]