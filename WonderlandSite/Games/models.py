from django.db import models
from datetime import date


class Game(models.Model):
    name = models.CharField("Назва", max_length=200)
    description = models.TextField("Опис")
    release_date = models.DateField("Дата виходу", default=date.today)
    main_image = models.ImageField("Головне фото", upload_to="game_main_photos/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Гра"
        verbose_name_plural = "Ігри"


class Review(models.Model):
    author_name = models.CharField("Ім'я автора", max_length=200)
    review_text = models.TextField("Текст")
    publish_date = models.DateField("Дата публікації", default=date.today)
    game = models.ForeignKey(Game, verbose_name="Гра", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author_name} {self.publish_date}'

    class Meta:
        verbose_name = "Огляд"
        verbose_name_plural = "Огляди"
