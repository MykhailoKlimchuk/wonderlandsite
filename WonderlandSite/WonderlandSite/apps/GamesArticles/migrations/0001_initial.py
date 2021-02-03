# Generated by Django 3.1.6 on 2021-02-01 18:07

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
                ('game_name', models.CharField(max_length=250, verbose_name='game name')),
                ('preview_photo', models.CharField(max_length=250, verbose_name='preview photo')),
                ('description', models.TextField(verbose_name='game description')),
                ('release_date', models.DateTimeField(verbose_name='game release date')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100, verbose_name='author name')),
                ('text', models.TextField(verbose_name='review text')),
                ('was_edit', models.BooleanField(verbose_name='was edit')),
                ('publish_date', models.DateTimeField(verbose_name='publish date')),
                ('Game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GamesArticles.game')),
            ],
        ),
    ]
