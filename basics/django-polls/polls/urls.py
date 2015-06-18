#To call our views, we need to map it to a URL - and for this we need a URLconf

from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    # ex: change the url to something else:
	# added the word 'specifics'
	# url(r'^specifics/(?P<poll_id>\d+)/$', views.detail, name='detail')
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
