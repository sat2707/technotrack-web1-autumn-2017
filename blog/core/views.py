# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import DetailView, ListView
from .models import Question, Category


class QuestionList(ListView):

    template_name = 'core/question_list.html'
    context_object_name = 'questions'
    model = Question


class QuestionDetail(DetailView):

    template_name = 'core/question_detail.html'
    context_object_name = 'question'
    model = Question


class CategoryDetail(DetailView):

    template_name = 'core/category_detail.html'
    context_object_name = 'category'
    model = Category


class CategoryList(ListView):

    template_name = 'core/category_list.html'
    context_object_name = 'categories'
    model = Category
