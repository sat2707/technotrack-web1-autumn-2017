from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^questions/$', views.QuestionList.as_view(), name='question_list'),
    url(r'^questions/(?P<pk>\d+)/$', views.QuestionDetail.as_view(), name='question_detail'),
    url(r'^categories/$', views.CategoryList.as_view(), name='category_list'),
    url(r'^categories/(?P<pk>\d+)/$', views.CategoryDetail.as_view(), name='category_detail'),
]
