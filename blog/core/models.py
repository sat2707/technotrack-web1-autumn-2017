# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):

    pass


class Category(models.Model):

    title = models.CharField(max_length=255, verbose_name=u'Название')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'


class Question(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Автор')
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    text = models.TextField(verbose_name=u'Текст')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='questions', verbose_name=u'Категории')
    is_deleted = models.BooleanField(default=False, verbose_name=u'Удалено?')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'


class Answer(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Автор')
    question = models.ForeignKey(Question, related_name='answers', verbose_name=u'Вопрос')
    text = models.TextField(default='', verbose_name=u'Текст')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{} ({})'.format(self.id, self.question.text)

    class Meta:
        verbose_name = u'Ответ'
        verbose_name_plural = u'Ответы'
