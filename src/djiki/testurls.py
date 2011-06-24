from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^wiki/', include('djiki.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
		)
