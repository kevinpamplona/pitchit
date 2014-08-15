from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin

#from pitchit.pages import views

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'pages.views.index'),
    url(r'^pitches/', include('pitches.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^assets/stylesheets/style.css', 'pages.views.stylesheet'),
)