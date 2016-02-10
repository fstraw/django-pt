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
		air = 'Yes'
		noise = 'Yes'
		ecology = 'Yes'
		archaeology = 'Yes'
		history = 'Yes'
		first_project = Project()
		first_project.epid = epid
		first_project.air = air
		first_project.noise = noise
		first_project.ecology = ecology
		first_project.archaeology = archaeology
		first_project.history = history
		first_project.save()
		
		saved_objects = Project.objects.all()
		first_saved_project = saved_objects[0]
		self.assertEqual(first_saved_project.epid, epid)
		self.assertEqual(first_saved_project.air, air)
		self.assertEqual(first_saved_project.noise, noise)
		self.assertEqual(first_saved_project.ecology, ecology)
		self.assertEqual(first_saved_project.archaeology, archaeology)
		self.assertEqual(first_saved_project.history, history)

class AddFormTests(TestCase):
	pass