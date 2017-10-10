# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Answer, Category


class AnswerInline(admin.TabularInline):

    model = Answer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = 'id', 'title',
    list_editable = 'title',
    inlines = AnswerInline,


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    pass
