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
	'south',
	'djiki',
]
ROOT_URLCONF = 'djiki.testurls'

DJIKI_IMAGES_PATH = 'djimages/'		# relative to MEDIA_ROOT
DJIKI_ALLOW_ANONYMOUS_EDITS = True

# The following switch will make all whitespaces appear as underscores
# in URLs. If you want to have nice URLs, leave it enabled. If you wish
# to keep distinction between space and underscore and have all page
# names verbatim, disable it.
DJIKI_SPACES_AS_UNDERSCORES = True