import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django_cherrypy",
    version = "1.0",
    url = '',
    license = 'BSD',
    description = "Cherrypy web server management command for Django.",
    long_description = read('README'),
    author = 'Matt Westerburg',
    author_email = 'matt.westerburg@comfychairconsulting.com',
    packages = ['django_cherrypy'],
    install_requires = ['setuptools'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
