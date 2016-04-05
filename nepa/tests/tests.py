from datetime import datetime, timedelta
from django.core.urlresolvers import resolve 
from django.test import TestCase 
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.test import Client

from nepa.views import home_page, add_page
from nepa.models import Project, Nepa, Noise, Air, Ecology, Aquatics, Archaeology, History


class HomePageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='test', email='test@test.com', password='test')
	def test_root_url_resolves_to_home_page_view(self):
		request = self.factory.get('/nepa/projects/')
		request.user = self.user
		response = home_page(request)
		self.assertEqual(response, home_page, response)
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
		##for get request
		request = HttpRequest()
		response = add_page(request)
		self.assertIn('Add Project', response.content.decode())

class ModelTests(TestCase):
	def test_saving_and_getting_projects(self):
		pass
	def test_project_model_saves(self):
		jobnumber = 'PBQ1601'
		projectname = 'US21 at Ralph McGill Road'
		projectnumber = 'STP00-0000-00(000)'
		pinumber = '0007678'
		projectmanager = 'Heather Perrin'
		county = 'Fulton'
		relatedprojects = ''
		project = Project()
		project.jobnumber = jobnumber
		project.projectname = projectname
		project.projectnumber = projectnumber
		project.pinumber = pinumber
		project.projectmanager = projectmanager
		project.county = county
		project.save()
		first_saved_project = Project.objects.all()[0]
		self.assertEqual(first_saved_project.jobnumber, jobnumber)
		self.assertEqual(first_saved_project.projectname, projectname)
		self.assertEqual(first_saved_project.projectnumber, projectnumber)
		self.assertEqual(first_saved_project.pinumber, pinumber)
		self.assertEqual(first_saved_project.projectmanager, projectmanager)
		self.assertEqual(first_saved_project.county, county)

	def test_can_add_new_nepa_project(self):
		pass
	def test_can_add_new_air_project(self):
		pass	
	def test_can_add_new_noise_project(self):
		pass
	def test_can_add_new_archaeology_project(self):
		pass
	def test_can_add_new_aquatics_project(self):
		pass
	def test_can_add_new_ecology_project(self):
		pass
	def test_can_add_new_history_project(self):
		pass
	def test_can_add_new_section4f_project(self):
		pass
	def test_can_edit_nepa_project(self):
		pass
	def test_can_edit_air_project(self):
		pass	
	def test_can_edit_noise_project(self):
		pass
	def test_can_edit_archaeology_project(self):
		pass
	def test_can_edit_aquatics_project(self):
		pass
	def test_can_edit_ecology_project(self):
		pass
	def test_can_edit_history_project(self):
		pass
	def test_can_edit_section4f_project(self):
		pass
	def test_redirect(self):
		pass

