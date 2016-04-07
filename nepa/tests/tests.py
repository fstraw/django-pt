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
        self.firstnepa = self.project.nepa_set.all()[0]
        self.nepaid = self.firstnepa.id
        self.nepatype = self.firstnepa.documenttype
    def test_root_url_resolves_to_home_page_view(self):
        request = self.factory.get(reverse('home'))
        request.user = self.user
        response = views.home_page(request)
        html = response.content.decode()
        self.assertTrue(b'<table id="id_project_table"' in html, html)
    def test_can_access_project_dash(self):
    	request = self.factory.get(reverse('project_dash', kwargs={'projectid' : self.project.id}))
        request.user = self.user
        response = views.project_dash(request, self.project.id)
        html = response.content.decode()        
        self.assertTrue(r'{} - {}'.format(self.project, self.project.projectname) in html, html)
    def test_can_access_nepa_dash(self):
    	request = self.factory.get(reverse('nepa_dash', kwargs={'projectid' : self.project.id, 'nepaid' : self.nepaid}))
        request.user = self.user
        response = views.nepa_dash(request, self.project.id, self.nepaid)
        html = response.content.decode()        
        self.assertTrue(r'{} - {} - {}'.format(self.project, self.project.projectname, self.nepatype) in html, html)
    def test_can_access_air_dash(self):
    	firstair = self.project.air_set.all()[0]
    	airid = firstair.id
    	airtype = firstair.documenttype
    	request = self.factory.get(reverse('air_dash', kwargs={'projectid' : self.project.id, 'airid' : airid}))
        request.user = self.user
        response = views.air_dash(request, self.project.id, airid)
        html = response.content.decode()        
        self.assertTrue(r'{} - {} - {}'.format(self.project, self.project.projectname, airtype) in html, html)
    def test_can_access_noise_dash(self):
    	firstnoise = self.project.noise_set.all()[0]
    	noiseid = firstnoise.id
    	noisetype = firstnoise.documenttype
    	request = self.factory.get(reverse('noise_dash', kwargs={'projectid' : self.project.id, 'noiseid' : noiseid}))
        request.user = self.user
        response = views.noise_dash(request, self.project.id, noiseid)
        html = response.content.decode()        
        self.assertTrue(r'{} - {} - {}'.format(self.project, self.project.projectname, noisetype) in html, html)
    def test_can_access_ecology_dash(self):
    	firstecology = self.project.ecology_set.all()[0]
    	ecologyid = firstecology.id
    	ecologytype = firstecology.documenttype
    	ecodoc = r'{} - {} - {}'.format(self.project, self.project.projectname, ecologytype)
    	request = self.factory.get(reverse('ecology_dash', kwargs={'projectid' : self.project.id, 'ecologyid' : ecologyid}))
        request.user = self.user
        response = views.ecology_dash(request, self.project.id, ecologyid)
        html = response.content.decode()
        self.assertTrue(ecodoc in html, html)
    def test_can_access_aquatics_dash(self):
    	firstaquatics = self.project.aquatics_set.all()[0]
    	aquaticsid = firstaquatics.id
    	aquaticstype = firstaquatics.documenttype
    	ecodoc = r'{} - {} - {}'.format(self.project, self.project.projectname, aquaticstype)
    	request = self.factory.get(reverse('aquatics_dash', kwargs={'projectid' : self.project.id, 'aquaticsid' : aquaticsid}))
        request.user = self.user
        response = views.aquatics_dash(request, self.project.id, aquaticsid)
        html = response.content.decode()
        self.assertTrue(ecodoc in html, html)
    def test_can_access_archaeology_dash(self):
    	firstarchaeology = self.project.archaeology_set.all()[0]
    	archaeologyid = firstarchaeology.id
    	archaeologytype = firstarchaeology.documenttype
    	ecodoc = r'{} - {} - {}'.format(self.project, self.project.projectname, archaeologytype)
    	request = self.factory.get(reverse('archaeology_dash', kwargs={'projectid' : self.project.id, 'archaeologyid' : archaeologyid}))
        request.user = self.user
        response = views.archaeology_dash(request, self.project.id, archaeologyid)
        html = response.content.decode()
        self.assertTrue(ecodoc in html, html)
    def test_can_access_history_dash(self):
    	firsthistory = self.project.history_set.all()[0]
    	historyid = firsthistory.id
    	historytype = firsthistory.documenttype
    	ecodoc = r'{} - {} - {}'.format(self.project, self.project.projectname, historytype)
    	request = self.factory.get(reverse('history_dash', kwargs={'projectid' : self.project.id, 'historyid' : historyid}))
        request.user = self.user
        response = views.history_dash(request, self.project.id, historyid)
        html = response.content.decode()
        self.assertTrue(ecodoc in html, html)
    def test_can_access_new_project_form(self):
        request = self.factory.get(reverse('add'))
        request.user = self.user
        response = views.add_page(request)
        html = response.content.decode()  
        self.assertTrue(r'Add/Edit Project' in html, html)
    def test_can_access_new_nepa_form(self):
    	request = self.factory.get(reverse('nepa_add', kwargs={'projectid': self.project.id}))
        request.user = self.user
        response = views.nepa_add(request, self.project.id)
        html = response.content.decode()  
        self.assertTrue(r'Add/Edit' in html, html)
    def test_can_access_new_air_form(self):
    	request = self.factory.get(reverse('air_add', kwargs={'projectid': self.project.id,
    										'ss_type' : 'air', 'form_type' : 'airform'}))
        request.user = self.user
        response = views.ss_add(request, self.project.id, 'air', 'airform')
        html = response.content.decode()  
        self.assertTrue(r'Add/Edit Air Document' in html, html)
    def test_can_access_new_noise_form(self):
    	request = self.factory.get(reverse('noise_add', kwargs={'projectid': self.project.id,
    										'ss_type' : 'noise', 'form_type' : 'noiseform'}))
        request.user = self.user
        response = views.ss_add(request, self.project.id, 'noise', 'noiseform')
        html = response.content.decode()  
        self.assertTrue(r'Add/Edit Noise Document' in html, html)
    def test_can_access_new_ecology_form(self):
    	request = self.factory.get(reverse('eco_add', kwargs={'projectid': self.project.id,
    										'ss_type' : 'ecology', 'form_type' : 'ecoform'}))
        request.user = self.user
        response = views.ss_add(request, self.project.id, 'ecology', 'ecoform')
        html = response.content.decode()  
        self.assertTrue(r'Add/Edit Ecology Document' in html, html)
    def test_can_access_new_aquatics_form(self):
    	request = self.factory.get(reverse('aquatics_add', kwargs={'projectid': self.project.id,
    										'ss_type' : 'aquatics', 'form_type' : 'aquaform'}))
        request.user = self.user
        response = views.ss_add(request, self.project.id, 'aquatics', 'aquaform')
        html = response.content.decode()  
        self.assertTrue(r'Add/Edit Aquatics Document' in html, html)
    def test_can_access_new_archaeology_form(self):
    	request = self.factory.get(reverse('archaeology_add', kwargs={'projectid': self.project.id,
    										'ss_type' : 'archaeology', 'form_type' : 'archform'}))
        request.user = self.user
        response = views.ss_add(request, self.project.id, 'archaeology', 'archform')
        html = response.content.decode()  
        self.assertTrue(r'Add/Edit Archaeology Document' in html, html)
    def test_can_access_new_history_form(self):
    	request = self.factory.get(reverse('history_add', kwargs={'projectid': self.project.id,
    										'ss_type' : 'history', 'form_type' : 'histform'}))
        request.user = self.user
        response = views.ss_add(request, self.project.id, 'history', 'histform')
        html = response.content.decode()  
        self.assertTrue(r'Add/Edit History Document' in html, html)
    def test_can_edit_existing_project_form(self):
        request = self.factory.get(reverse('project_edit', kwargs={'projectid': self.project.id}))
        request.user = self.user
        response = views.project_edit(request, self.project.id)
        html = response.content.decode()  
        self.assertTrue(r'Add/Edit Project' in html, html)
    def test_can_edit_existing_nepa_form(self):
        request = self.factory.get(reverse('nepa_edit', kwargs={'projectid': self.project.id, 'nepaid': self.nepaid}))
        request.user = self.user
        response = views.nepa_edit(request, self.project.id, self.nepaid)
        html = response.content.decode()  
        self.assertTrue(r'Add/Edit Environmental Document' in html, html)
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