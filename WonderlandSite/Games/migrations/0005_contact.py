# Generated by Django 3.1.6 on 2021-02-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0004_galleryphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="Ім'я того хто звернувся")),
                ('email', models.CharField(max_length=200, verbose_name='Пошта')),
                ('subject', models.CharField(max_length=200, verbose_name='Тема')),
                ('message', models.TextField(verbose_name='Повідомлення')),
            ],
            options={
                'verbose_name': 'Повідомлення',
                'verbose_name_plural': 'Повідомлення',
            },
        ),
    ]
