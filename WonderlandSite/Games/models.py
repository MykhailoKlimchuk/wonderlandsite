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
    publish_date = models.DateTimeField("Дата публікації")
    game = models.ForeignKey(Game, verbose_name="Гра", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author_name} {self.publish_date}'

    class Meta:
        verbose_name = "Огляд"
        verbose_name_plural = "Огляди"


class Teammate(models.Model):
    name = models.CharField("Ім'я працівника", max_length=200)
    position = models.CharField("Посада", max_length=200)
    photo = models.ImageField("Фото працівника", upload_to="teammate_photos/")

    # todo добавити опис працівника і посилання на соцмережі

    def __str__(self):
        return f'{self.name} {self.position}'

    class Meta:
        verbose_name = "Працівник"
        verbose_name_plural = "Працівники"


class GalleryPhoto(models.Model):
    photo = models.ImageField("Фото з галереї", upload_to="gallery_photo/")

    class Meta:
        verbose_name = "Фотографія з галереї"
        verbose_name_plural = "Фотографії галереї"


class Contact(models.Model):
    name = models.CharField("Ім'я того хто звернувся", max_length=200)
    email = models.CharField("Пошта", max_length=200)
    subject = models.CharField("Тема", max_length=200)
    message = models.TextField("Повідомлення")

    def __str__(self):
        return f'{self.name} {self.subject}'

    class Meta:
        verbose_name = "Повідомлення"
        verbose_name_plural = "Повідомлення"

