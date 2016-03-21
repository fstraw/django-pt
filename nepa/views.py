from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import RequestContext, loader
from nepa.forms import ProjectForm, NepaForm, PlannerForm, AirForm
from nepa.models import Project, Nepa, ProjectNumbers, PINumbers

def home_page(request):	
	if request.method == 'GET':
		project_list = Project.objects.all()
		planner_form = PlannerForm()
	elif request.method == 'POST':
		planner_form = PlannerForm(request.POST)
		try:
			"""Dirty hack to handle post redirect from add_page :-/ """
			project_list = Project.objects.filter(projectmanager=request.POST['pm'])
		except:
			project_list = Project.objects.all()
	context = RequestContext(request, {'project_list' : project_list,
										'planner_form' : planner_form})
	template = loader.get_template('home.html')
	return HttpResponse(template.render(context))

def add_page(request):
	if request.method == 'POST':
		project_form = ProjectForm(request.POST)
		if project_form.is_valid():
			# return HttpResponse('<html>{}</html>'.format('bleh'))
			project_data = project_form.cleaned_data
			project = Project()
			project.jobnumber = project_data['jobnumber']
			project.projectname = project_data['projectname']
			project.projectmanager = project_data['projectmanager']
			project.projectdescription = project_data['projectdescription']
			project.county = project_data['county']
			project.comments = project_data['comments']
			project.save() ##Need to save project object before adding PIs and PNs
			for num in project_data['pinumber'].split(','):
				pi = PINumbers.objects.get_or_create(pi_number=num)[0]					
				project.pis.add(pi)
			for num in project_data['projectnumber'].split(','):
				pn = ProjectNumbers.objects.get_or_create(project_number=num)[0]					
				project.projectnumbers.add(pn)
			blank_request = HttpRequest()
			blank_request.method = 'GET'
			return redirect(home_page)
		else:
			## need to fix error checking			
			return render(request, 'add_project.html', {'project_form' : project_form})
	else:
		return render(request, 'add_project.html', {'project_form' : ProjectForm })

def project_dash(request, projectid):
	project = get_object_or_404(Project, id=projectid)

	context = { 
				'project': project,				
			}
	return render(request, 'projectdash.html', context)

def nepa_dash(request, projectid, nepaid):
	project = get_object_or_404(Project, id=projectid)
	nepa = project.nepa_set.all().get(id=nepaid)
	context = { 
				'project' : project,
				'nepa': nepa,				
			}
	return render(request, 'nepadash.html', context)

def air_dash(request, projectid, airid):
	project = get_object_or_404(Project, id=projectid)
	air = project.air_set.all().get(id=airid)
	context = { 
				'project' : project,
				'air': air,				
			}
	return render(request, 'airdash.html', context)
	

def project_edit(request, projectid):
	''' Should only come from edit page, so nepa should update automagically '''
	project = get_object_or_404(Project, id=projectid)
	if request.method == 'POST':
		if request.POST.get('delete'):
			project.delete()
			blank_request = HttpRequest()
			blank_request.method = 'GET'
			return redirect(home_page)
		project_form = ProjectForm(request.POST, instance=project)
		attached_pis = [i.pi_number for i in project.pis.all()]
		attached_pns = [pn.project_number for pn in project.projectnumbers.all()]
		# return HttpResponse('<html>{}</html>'.format(attached_pns))
		if project_form.is_valid():
			clean = project_form.cleaned_data
			# if not clean['pinumber']=='':
			for num in attached_pis:
				pi = PINumbers.objects.get(pi_number=num)
				project.pis.remove(pi)
			for num in clean['pinumber'].split(','):
				pi = PINumbers.objects.get_or_create(pi_number=num)[0]					
				project.pis.add(pi)
			for num in attached_pns:
				pn = ProjectNumbers.objects.get(project_number=num)
				project.projectnumbers.remove(pn)
			for num in clean['projectnumber'].split(','):
				pn = ProjectNumbers.objects.get_or_create(project_number=num)[0]					
				project.projectnumbers.add(pn)
			##add PI and PN cleanup, check for orphans
			# return HttpResponse('<html>{}</html>'.format(pi))
			project_form.save() #save and commit job number to db			
			return redirect('project_dash', projectid=project.id)
		return render(request, 'add_project.html', {'project_form' : project_form})
	else:		
		project_form = ProjectForm(instance=project)
		return render(request, 'add_project.html', {'project_form' : project_form})

def nepa_edit(request, projectid, nepaid):
	project = get_object_or_404(Project, id=projectid)
	nepa = project.nepa_set.all().get(id=nepaid)
	if request.method == 'POST':
		if request.POST.get('delete'):
			nepa.delete()
			blank_request = HttpRequest()
			blank_request.method = 'GET'
			return project_dash(blank_request, projectid)
		form = NepaForm(request.POST, instance=nepa)
		if form.is_valid():
			##fix nepa project change functionality
			form.save() #save and commit job number to db			
			return redirect('nepa_dash', projectid=project.id, nepaid=nepa.id)
		return render(request, 'add_document.html', {'form':form})
	else:		
		form = NepaForm(instance=nepa)
		return render(request, 'add_document.html', {'form':form})

def nepa_add(request, projectid):
	project = get_object_or_404(Project, id=projectid)
	if request.method == 'POST':
		form = NepaForm(request.POST)
		if form.is_valid():
			##fix nepa project change functionality
			form.save() #save and commit job number to db			
			return redirect('project_dash', projectid=project.id)
		return render(request, 'add_document.html', {'form':form})
	else:
		form = NepaForm(initial={'project':project})	
		return render(request, 'add_document.html', {'form':form, 'project':project})

def air_add(request, projectid):
	project = get_object_or_404(Project, id=projectid)
	if request.method == 'POST':
		air_form = AirForm(request.POST)
		if air_form.is_valid():
			##fix nepa project change functionality
			air_form.save() #save and commit job number to db			
			return redirect('project_dash', projectid=project.id)
		return render(request, 'add_document.html', {'form':air_form})
	else:
		air_form = AirForm(initial={'project':project})	
		return render(request, 'add_document.html', {'form':air_form, 'project':project})

def air_edit(request, projectid, airid):
	project = get_object_or_404(Project, id=projectid)
	air = project.air_set.all().get(id=airid)
	if request.method == 'POST':
		if request.POST.get('delete'):
			air.delete()
			blank_request = HttpRequest()
			blank_request.method = 'GET'
			return project_dash(blank_request, projectid)
		form = AirForm(request.POST, instance=air)
		if form.is_valid():
			##fix air project change functionality
			form.save() #save and commit job number to db			
			return redirect('air_dash', projectid=project.id, airid=air.id)
		return render(request, 'add_document.html', {'form':form})
	else:		
		form = AirForm(instance=air)
		return render(request, 'add_document.html', {'form':form})
