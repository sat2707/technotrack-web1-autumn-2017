from django.conf.urls import url
from core import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^questions/$', views.QuestionList.as_view(), name='question_list'),
    url(r'^questions/new/$', login_required(views.NewQuestion.as_view()), name='new_question'),
    url(r'^questions/(?P<pk>\d+)/$', views.QuestionDetail.as_view(), name='question_detail'),
    url(r'^questions/(?P<pk>\d+)/edit/$', login_required(views.QuestionUpdate.as_view()), name='question_update'),
    url(r'^categories/$', views.CategoryList.as_view(), name='category_list'),
    url(r'^categories/(?P<pk>\d+)/$', views.CategoryDetail.as_view(), name='category_detail'),
]
