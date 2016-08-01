=====
pt
=====

pt is a simple demo of Django's basic usage.

Description
-----------

pt is a simple, Django-powered project tracking solution.

Documentation
-------------

Coming soon!

Quickstart
----------

1. Add "pt" to INSTALLED_APPS:
  INSTALLED_APPS = {
    ...
    'pt'
  }

2. Include the pt URLconf in urls.py:
  url(r'^pt/', include('pt.urls'))

3. Run `python manage.py makemigrations` to create pt's models.

4. Run `python manage.py migrate` to migrate pt's models.

5. Run `python manage.py createsuperuser` to set up initial login.

6. Run the development server and access http://127.0.0.1:8000 to
    access project dashboard.

7. Start tracking!