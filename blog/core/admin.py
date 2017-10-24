# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from .models import Question, Answer, Category, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    pass


class AnswerInline(admin.TabularInline):

    model = Answer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = 'id', 'title'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = 'id', 'title', 'author'
    inlines = AnswerInline,


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    list_display = 'id', 'question', 'author'
