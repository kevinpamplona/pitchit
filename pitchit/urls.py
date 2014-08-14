from django.conf.urls import patterns, include, url

from django.contrib import admin

#from pitchit.pages import views

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'pages.views.index'),
    url(r'^pitches/', include('pitches.urls')),
    url(r'^admin/', include(admin.site.urls)),
)