from django.conf.urls.defaults import *
from . import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='djiki-index'),
	url(r'^(?P<title>[^/]+)$', views.view, name='djiki-page-view'),
	url(r'^(?P<title>[^/]+)/edit/$', views.edit, name='djiki-page-edit'),
	url(r'^(?P<title>[^/]+)/history/$', views.history, name='djiki-page-history'),
	url(r'^(?P<title>[^/]+)/history/(?P<revision_pk>[0-9]+)/$', views.view, name='djiki-page-revision'),
	url(r'^(?P<title>[^/]+)/diff/$', views.diff, name='djiki-page-diff'),
	url(r'^(?P<title>[^/]+)/undo/(?P<revision_pk>[0-9]+)/$', views.undo, name='djiki-page-undo'),
	url(r'^(?P<title>[^/]+)/revert/(?P<revision_pk>[0-9]+)/$', views.revert, name='djiki-page-revert'),
	)
