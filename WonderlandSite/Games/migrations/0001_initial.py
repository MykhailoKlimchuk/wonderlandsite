# Generated by Django 3.1.6 on 2021-02-04 15:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Назва')),
                ('description', models.TextField(verbose_name='Опис')),
                ('release_date', models.DateField(default=datetime.date.today, verbose_name='Дата виходу')),
                ('main_image', models.ImageField(upload_to='game_main_photos/', verbose_name='Головне фото')),
            ],
            options={
                'verbose_name': 'Гра',
                'verbose_name_plural': 'Ігри',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200, verbose_name="Ім'я автора")),
                ('review_text', models.TextField(verbose_name='Текст')),
                ('publish_date', models.DateTimeField(default=datetime.date.today, verbose_name='Дата публікації')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Games.game', verbose_name='Гра')),
            ],
            options={
                'verbose_name': 'Огляд',
                'verbose_name_plural': 'Огляди',
            },
        ),
    ]
