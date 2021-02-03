from django.db import models


class Game(models.Model):
    game_name = models.CharField('game name', max_length=250)
    preview_photo = models.ImageField(upload_to='')
    description = models.TextField('game description')
    release_date = models.DateTimeField('game release date')


class Review(models.Model):
    Game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author_name = models.CharField('author name', max_length=100)
    text = models.TextField('review text')
    was_edit = models.BooleanField('was edit')
    publish_date = models.DateTimeField('publish date')



