import os
from setuptools import setup, find_packages

setup(
    name = "django_cherrypy",
    version = "1.0",
    url = '',
    license = 'BSD',
    description = "Cherrypy web server management command for Django.",
    long_description = "Cherrpy webserver as a management command for Django",
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
