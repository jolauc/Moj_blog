from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns, include, url

admin.autodiscover()


urlpatterns = patterns('',
   url(r'^admin/', include(admin.site.urls)),
   url(r'^/?$', 'news.views.index'),)


    # Examples:
    #url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^news/', include('news.urls')),
	#


