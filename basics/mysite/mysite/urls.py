#note - this is the URLconf for the PROJECT

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	   	url(r'^polls/',include('polls.urls',namespace="polls")),
		url(r'^admin/',include(admin.site.urls)),
	) #we are pointing the root URLconf(in this file) at the polls.urls module
#the url() function is passed four arguments, two required: regex and view, and two optional: kwargs, and name

	
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#url(r'^admin/', include(admin.site.urls)),)
