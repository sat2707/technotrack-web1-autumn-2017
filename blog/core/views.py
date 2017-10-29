# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import DetailView, ListView, CreateView, UpdateView
from .models import Question, Category
from django import forms
from django.db import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, render, reverse, redirect


class QuestionUpdate(UpdateView):

    template_name = 'core/edit_question.html'
    model = Question
    fields = 'title', 'text'

    def get_queryset(self):
        return super(QuestionUpdate, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse('core:question_detail', kwargs={'pk': self.object.pk})


class NewQuestion(CreateView):

    template_name = 'core/new_question.html'
    model = Question
    fields = 'title', 'text', 'categories'

    def get_success_url(self):
        return reverse('core:question_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NewQuestion, self).form_valid(form)


def test(request):
    return HttpResponse(request.session['blabla'])


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


class CategoriesListForm(forms.Form):

    order_by = forms.ChoiceField(choices=(
        ('title', 'Title asc'),
        ('-title', 'Title desc'),
        ('id', 'ID'),
    ), required=False)
    search = forms.CharField(required=False)
    threshold = forms.IntegerField(required=False)


class CategoryList(ListView):

    template_name = 'core/category_list.html'
    context_object_name = 'categories'
    model = Category

    def get_queryset(self):

        q = super(CategoryList, self).get_queryset()

        self.form = CategoriesListForm(self.request.GET)

        if self.form.is_valid():
            if self.form.cleaned_data['threshold']:
                q = q.annotate(question_count=models.Count('questions__id')).filter(question_count__gt=self.form.cleaned_data['threshold'])
            if self.form.cleaned_data['order_by']:
                q = q.order_by(self.form.cleaned_data['order_by'])
            if self.form.cleaned_data['search']:
                q = q.filter(title=self.form.cleaned_data['search'])
        return q

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['searchform'] = self.form
        return context
