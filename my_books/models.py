from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Название книги')
    author = models.CharField(max_length=200, null=True, blank=True, verbose_name='Автор')
    genre = models.CharField(max_length=200, null=True, blank=True, verbose_name='Жанр')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    is_complete = models.BooleanField(default=False, verbose_name='Прочитано')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    verbose_name = 'Книга'
    verbose_name_plural = 'Книги'
    ordering = ['title']
