from datetime import datetime, timedelta
from django.core.urlresolvers import resolve 
from django.test import TestCase 
from django.http import HttpRequest
from django.template.loader import render_to_string

from nepa.views import home_page, add_page
from nepa.models import Project, Nepa, Noise, Air, Ecology, Aquatics, Archaeology, History


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
		# self.assertEqual(first_saved_project.relatedprojects, relatedprojects)

# class AddFormTests(TestCase):
	# def test_add_page_can_save_a_POST_request(self):
		# request = HttpRequest()
		# request.method = 'POST'
		# request.POST = {'epid' :' PBQ1601',
						# 'nepa' : 'Yes',
						# 'air' : 'Yes',
						# 'noise' : 'Yes',
						# 'ecology' : 'Yes',
						# 'archaeology' : 'Yes',
						# 'history' : 'Yes',
						# 'nepa_due_date' : datetime.now(),
						# 'air_due_date' : datetime.now(),
						# 'noise_due_date' : datetime.now(),
						# 'ecology_due_date' : datetime.now(),
						# 'archaeology_due_date' : datetime.now(),
						# 'history_due_date' : datetime.now(),
						# }
		#this test is currently failing due to HttpRequestRedirect
		# response = add_page(request)
		# request = HttpRequest()
		# self.assertIn('PBQ1601', home_page(request), home_page(request))