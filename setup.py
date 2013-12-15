from setuptools import setup, find_packages, Command

import django_worldbank

setup(
    name = "django-worldbank",
    version = django_worldbank.__version__,
    packages = find_packages(),
    author = "Chris Spencer",
    author_email = "chrisspen@gmail.com",
    description = "",
    license = "LGPL",
    url = "https://github.com/chrisspen/django_worldbank",
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: LGPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires = ['Django>=1.4', 'wbpy', 'django_data_mirror'],
)
