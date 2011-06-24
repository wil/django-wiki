import os

from setuptools import setup, find_packages

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = 'django-wiki',
	version = '0.4',
	url = 'http://github.com/myles/django-wiki',
	license = 'BSD License',
	description = 'A Django wiki application.',
	long_description = read('README.rst'),
	
	packages = find_packages('src'),
	package_dir = {'': 'src'},
	
	install_requires = [
		'setuptools',
		'creole',
	],
	
	classifiers = [
		'Development Status :: 4 - Beta',
		'Framework :: Django',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Internet :: WWW/HTTP',
	],
)
