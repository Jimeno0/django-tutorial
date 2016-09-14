from django.conf.urls import url
from . import views


app_name = 'polls'
# urlpatterns = [
#   url(r'^$', views.index, name='index'),
#   url(r'^(?P<question_id>[0-9]+)/$', views.details, name='details'),
#   url(r'^(?P<question_id>[0-9]+)/results/$', views.result, name='result'),
#   url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]

urlpatterns = [
  url(r'^$', views.indexView.as_view(), name='index'),
  url(r'^(?P<pk>[0-9]+)/$', views.detailsView.as_view(), name='details'),
  url(r'^(?P<pk>[0-9]+)/results/$', views.resultView.as_view(), name='result'),
  url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]