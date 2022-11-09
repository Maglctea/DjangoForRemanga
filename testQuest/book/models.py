from django.db import models
from setuptools.command.egg_info import manifest_maker


class Tag(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название')

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class Title(models.Model):
    ru_name = models.CharField(max_length=150, verbose_name='Русское название', unique=True)
    eng_name = models.CharField(max_length=150, verbose_name='Английское название', unique=True)
    alt_name = models.CharField(max_length=150, blank=True, verbose_name='Альтернативное название', unique=True)
    description = models.TextField(verbose_name='Описание')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.ru_name


class Volume(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, verbose_name='Название книги', related_name='volumes')
    name = models.CharField(max_length=150, verbose_name='Название тома')
    price = models.PositiveBigIntegerField(default=0, verbose_name='Цена')
    number = models.PositiveIntegerField(verbose_name='Номер тома')

    class Meta:
        verbose_name = "Том"
        verbose_name_plural = "Томы"

    def __str__(self):
        return f'{self.title.ru_name} - Том {self.number}'


class Chapter(models.Model):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, verbose_name='Том', related_name='chapters')
    number = models.PositiveIntegerField(verbose_name='Номер главы')
    content = models.TextField(verbose_name='Текст')
    views_counter = models.PositiveIntegerField(default=0, verbose_name='Кол-во просмотров')
    like_counter = models.PositiveIntegerField(default=0, verbose_name='Кол-во лайков')

    class Meta:
        verbose_name = "Глава"
        verbose_name_plural = "Главы"

    def __str__(self):
        return f'{self.volume}, Глава {self.number}'
