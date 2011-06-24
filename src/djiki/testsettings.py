DEBUG = True
DEBUG_TEMPLATE = True
SITE_ID = 1
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': '/tmp/django-wiki-devel.db',
	}
}
INSTALLED_APPS = [
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.admin',
	'django.contrib.admindocs',
	'django.contrib.comments',
	'django.contrib.staticfiles',
	'south',
	'djiki',
]
STATIC_URL = '/static/'
ROOT_URLCONF = 'djiki.testurls'
DJIKI_ALLOW_ANONYMOUS_EDITS = True
DJIKI_SPACES_AS_UNDERSCORES = True