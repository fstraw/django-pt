"""eptrack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import eptrack

urlpatterns = [
	url(r'^$', 'nepa.views.home_page', name='home'),
	url(r'^add/$', 'nepa.views.add_page', name='add'),
    url(r'^admin/$', include(admin.site.urls)),
    url(r'(?P<projectid>[0-9]+)/$', 'nepa.views.project_dash', name='project_dash'),
	url(r'(?P<projectid>[0-9]+)/nepa/$', 'nepa.views.nepa_dash', name='nepa_dash'),
    url(r'(?P<projectid>[0-9]+)/edit/$', 'nepa.views.project_edit', name='project_edit'),	
    ]