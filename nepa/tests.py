from django.core.urlresolvers import resolve 
from django.test import TestCase 
from django.http import HttpRequest
from django.template.loader import render_to_string

from nepa.views import home_page, add_page
from nepa.models import Project


class HomePageTest(TestCase): 
	def test_root_url_resolves_to_home_page_view(self): 
		found = resolve('/')
		self.assertEqual(found.func, home_page)
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)

class NewProjectTest(TestCase):
	def test_url_resolves_to_add_project_view(self):
		found = resolve('/add/')
		self.assertEqual(found.func, add_page)
	def test_add_page_returns_correct_html(self):
		request = HttpRequest()
		response = add_page(request)
		expected_html = render_to_string('add.html')
		self.assertEqual(response.content.decode(), expected_html)

class ModelTests(TestCase):
	def test_saving_and_getting_projects(self):
		epid = 'PBQ1601'
		first_project = Project()
		first_project.epid = epid
		first_project.save()
		
		saved_objects = Project.objects.all()
		first_saved_project = saved_objects[0]
		self.assertEqual(first_saved_project.epid, epid)