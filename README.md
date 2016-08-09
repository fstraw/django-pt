=====
pt
=====

pt is a simple, Django-powered project tracking solution.

[![Build Status](https://travis-ci.org/fstraw/django-pt.svg?branch=master)](https://travis-ci.org/fstraw/django-pt)

Documentation
-------------

Coming soon!

Demo
----

[http://www.lowestfrequency.com/pt](http://lowestfrequency.com/pt "PT Demo")


Quickstart
----------

1. Add `pt` to `INSTALLED_APPS` in `settings.py`:

> 		INSTALLED_APPS = {
> 		...
> 		'pt'
> 		}

Add 'pt/templates/pt' to `TEMPLATES` in `settings.py`:

>       TEMPLATES = [
> 	    {
> 	        'BACKEND': 'django.template.backends.django.DjangoTemplates',
> 	        'DIRS': ['pt/templates/pt/'],
> 	        ...
> 	        }

Add '/login/' to `LOGIN_URL` in `settings.py`:

>       LOGIN_URL = '/login/'

Include the `pt` URLconf in urls.py:
  
>       url(r'^pt/', include('pt.urls'))


2. Run `python manage.py makemigrations` to create pt's models.

3. Run `python manage.py migrate` to migrate pt's models.

4. Run `python manage.py createsuperuser` to set up initial login.

5. Start tracking!