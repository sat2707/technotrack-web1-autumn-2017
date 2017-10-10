from django.conf.urls import url
from core.views import post_detail, CategoryDetail, question_list

urlpatterns = [
    url(r'^questions/$', question_list, name='question_list'),
    url(r'^questions/(?P<pk>\d+)/$', post_detail, name='question_detail'),
    url(r'^categories/(?P<pk>\d+)/$', CategoryDetail.as_view()),
]
