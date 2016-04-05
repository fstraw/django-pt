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
import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	url(r'^$', views.home_page, name='home'),
	url(r'^add/$', views.add_page, name='add'),
    ##Dashboards
    url(r'^(?P<projectid>[0-9]+)/$', views.project_dash, name='project_dash'),    
    url(r'^(?P<projectid>[0-9]+)/(?P<nepaid>[0-9]+)/$', views.nepa_dash, name='nepa_dash'),
    url(r'^(?P<projectid>[0-9]+)/air/(?P<airid>[0-9]+)/$', views.air_dash, name='air_dash'),
    url(r'^(?P<projectid>[0-9]+)/noise/(?P<noiseid>[0-9]+)/$', views.noise_dash, name='noise_dash'),
    ##Edit, make names unique
    url(r'^(?P<projectid>[0-9]+)/edit/$', views.project_edit, name='project_edit'),
    url(r'^(?P<projectid>[0-9]+)/(?P<nepaid>[0-9]+)/edit$', views.nepa_edit, name='nepa_edit'),
    url(r'^(?P<projectid>[0-9]+)/air/(?P<ssid>[0-9]+)/edit$', views.ss_edit, {'ss_type' : 'air', 'form_type' : 'airform'}, name='air_edit'),
    url(r'^(?P<projectid>[0-9]+)/noise/(?P<ssid>[0-9]+)/edit$', views.ss_edit, {'ss_type' : 'noise', 'form_type' : 'noiseform'}, name='noise_edit'),
    ##Add, make names unique
    url(r'^(?P<projectid>[0-9]+)/nepa/add/$', views.nepa_add, name='nepa_add'),
    url(r'^(?P<projectid>[0-9]+)/air/add/$', views.ss_add, {'ss_type' : 'air', 'form_type' : 'airform'}, name='air_add'),
    url(r'^(?P<projectid>[0-9]+)/noise/add/$', views.ss_add, {'ss_type' : 'noise', 'form_type' : 'noiseform'}, name='noise_add'),
    ]