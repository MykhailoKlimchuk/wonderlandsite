# Generated by Django 3.1.6 on 2021-02-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamesArticles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='preview_photo',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
