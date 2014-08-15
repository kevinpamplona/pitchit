from django.conf.urls import patterns, url

from pitches import views
from views import RenderView

urlpatterns = patterns('',
	url(r'^post$', RenderView.as_view(), name='render'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pitch_id>\d+)/$', views.detail, name='detail'),
)