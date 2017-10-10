# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404
from .models import Question, Category


def question_list(request):

    questions = Question.objects.all()
    return render(request, 'core/question_list.html', {'questions': questions})


def post_detail(request, pk=None):

    question = get_object_or_404(Question.objects.all(), pk=pk)

    return render(request, 'core/post_detail.html', {'question': question})


class CategoryDetail(DetailView):

    template_name = 'core/category_detail.html'
    context_object_name = 'category'
    model = Category
