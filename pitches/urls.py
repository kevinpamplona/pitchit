from django.conf.urls import patterns, url

from pitches import views
from views import RenderView

urlpatterns = patterns('',
	url(r'^post$', RenderView.as_view(), name='render'),
	url(r'^kudos/post$', RenderView.as_view(), name='increase'),
	url(r'^get$', RenderView.as_view(), name='increase'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pitch_id>\d+)/$', views.detail, name='detail'),
)