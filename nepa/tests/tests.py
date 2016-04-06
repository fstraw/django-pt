from datetime import datetime, timedelta
from unittest import skip
from django.core.urlresolvers import resolve, reverse
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.template.loader import render_to_string
from nepa import views
from nepa.models import Project, Nepa, Noise, Air, Ecology, Aquatics, Archaeology, History
from utils import clear_database, add_dummy_data

class ViewsTest(TestCase):
    def setUp(self):
    	add_dummy_data(1)
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test', email='test@test.com', password='test')        
        self.project = Project.objects.all()[0]
    def test_root_url_resolves_to_home_page_view(self):
        request = self.factory.get(reverse('home'))
        request.user = self.user
        response = views.home_page(request)
        html = response.content.decode()
        self.assertTrue(b'<table id="id_project_table"' in html, html)
    def test_add_project_url_resolves_to_form(self):
        request = self.factory.get(reverse('add'))
        request.user = self.user
        response = views.add_page(request)
        html = response.content.decode()  
        self.assertTrue(r'Add/Edit Project' in html, html)
    def test_can_access_project_dash(self):
    	request = self.factory.get(reverse('project_dash', kwargs={'projectid' : self.project.id}))
        request.user = self.user
        response = views.project_dash(request, self.project.id)
        html = response.content.decode()        
        self.assertTrue(r'{} - {}'.format(self.project, self.project.projectname)  in html, html)
    def test_can_access_nepa_dash(self):
    	firstnepa = self.project.nepa_set.all()[0]
    	nepaid = firstnepa.id
    	nepatype = firstnepa.documenttype
    	request = self.factory.get(reverse('nepa_dash', kwargs={'projectid' : self.project.id, 'nepaid' : nepaid}))
        request.user = self.user
        response = views.nepa_dash(request, self.project.id, nepaid)
        html = response.content.decode()        
        self.assertTrue(r'{} - {} - {}'.format(self.project, self.project.projectname, nepatype)  not in html, html)
    def test_add_nepa_url_resolves_to_form(self):
    	request = self.factory.get(reverse('nepa_add', kwargs={'projectid': self.project.id}))
        request.user = self.user
        response = views.nepa_add(request, self.project.id)
        html = response.content.decode()  
        self.assertTrue(r'Add/Edit' in html, html)

# class NewProjectTest(TestCase):
# 	def test_url_resolves_to_add_project_view(self):
# 		found = resolve('/add/')
# 		self.assertEqual(found.func, add_page)
# 	def test_add_page_returns_correct_html(self):
# 		##for get request
# 		request = HttpRequest()
# 		response = add_page(request)
# 		self.assertIn('Add Project', response.content.decode())

# class ModelTests(TestCase):
# 	def test_saving_and_getting_projects(self):
# 		pass
# 	def test_project_model_saves(self):
# 		jobnumber = 'PBQ1601'
# 		projectname = 'US21 at Ralph McGill Road'
# 		projectnumber = 'STP00-0000-00(000)'
# 		pinumber = '0007678'
# 		projectmanager = 'Heather Perrin'
# 		county = 'Fulton'
# 		relatedprojects = ''
# 		project = Project()
# 		project.jobnumber = jobnumber
# 		project.projectname = projectname
# 		project.projectnumber = projectnumber
# 		project.pinumber = pinumber
# 		project.projectmanager = projectmanager
# 		project.county = county
# 		project.save()
# 		first_saved_project = Project.objects.all()[0]
# 		self.assertEqual(first_saved_project.jobnumber, jobnumber)
# 		self.assertEqual(first_saved_project.projectname, projectname)
# 		self.assertEqual(first_saved_project.projectnumber, projectnumber)
# 		self.assertEqual(first_saved_project.pinumber, pinumber)
# 		self.assertEqual(first_saved_project.projectmanager, projectmanager)
# 		self.assertEqual(first_saved_project.county, county)
		## self.assertEqual(first_saved_project.relatedprojects, relatedprojects)

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