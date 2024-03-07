from django.db import models

from users.models import DoitUser
from .enums import ArticleType, ArticleStatus
from .constants import DEFAULT_LENGTH_CHAR_FIELD, TITLE_LENGTH_CHAR_FIELD, DEFAULT_LENGTH_VIEW_STRING


class Category(models.Model):
    name = models.CharField(max_length=DEFAULT_LENGTH_CHAR_FIELD, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=TITLE_LENGTH_CHAR_FIELD, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    author = models.ForeignKey(DoitUser, on_delete=models.CASCADE, related_name='articles', verbose_name='Автор')
    categories = models.ManyToManyField(Category, related_name='articles', verbose_name='Категории')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    published_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата публикации')
    type = models.CharField(max_length=DEFAULT_LENGTH_CHAR_FIELD, choices=ArticleType.choices(), verbose_name='Тип')
    status = models.CharField(
        max_length=DEFAULT_LENGTH_CHAR_FIELD,
        choices=ArticleStatus.choices(),
        verbose_name='Статус',
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title[:DEFAULT_LENGTH_VIEW_STRING]
