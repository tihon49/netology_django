# Generated by Django 2.2.10 on 2020-06-17 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20200617_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.CreateModel(
            name='StudenTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Teacher')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(through='school.StudenTeacher', to='school.Teacher'),
        ),
    ]
