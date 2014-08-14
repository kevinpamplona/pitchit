from django.conf.urls import patterns, url

from pitches import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pitch_id>\d+)/$', views.detail, name='detail'),
)