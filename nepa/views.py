from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from nepa.forms import ProjectForm, NepaForm, PlannerForm
from nepa.models import Project, Nepa, ProjectNumbers, PINumbers

def home_page(request):	
	if request.method == 'GET':
		project_list = Project.objects.all()
		planner_form = PlannerForm()
	elif request.method == 'POST':
		planner_form = PlannerForm(request.POST)
		project_list = Project.objects.filter(projectmanager=request.POST['pm'])	
	context = RequestContext(request, {'project_list' : project_list,
										'planner_form' : planner_form})
	template = loader.get_template('home.html')
	return HttpResponse(template.render(context))

def add_page(request):
	if request.method == 'POST':
		project_form = ProjectForm(request.POST)
		nepa_form = NepaForm(request.POST)
		nepa_form.is_valid() ##generate cleaned_data attribute
		if project_form.is_valid():
			# return HttpResponse('<html>{}</html>'.format('bleh'))
			project_data = project_form.cleaned_data
			nepa_data = nepa_form.cleaned_data			
			project = Project()
			nepa = Nepa()
			project.jobnumber = project_data['jobnumber']
			project.projectname = project_data['projectname']
			project.projectmanager = project_data['projectmanager']
			project.projectdescription = project_data['projectdescription']
			project.county = project_data['county'] 
			# project.pis = project_data['pis'] #not working
			# project.projectnumbers = project_data['projectnumbers'] #not working
			project.comments = project_data['comments'] 
			project.save()
			nepa_data['project'] = project
			nepa.project = project
			nepa.specialist = nepa_data['specialist']
			nepa.stateplanner = nepa_data['stateplanner']
			nepa.documenttype = nepa_data['documenttype']
			nepa.earlycoordination = nepa_data['earlycoordination']
			nepa.statedraft = nepa_data['statedraft']
			nepa.stateapproval = nepa_data['stateapproval']
			nepa.fhwadraft = nepa_data['fhwadraft']
			nepa.fhwaapproval = nepa_data['fhwaapproval']
			nepa.statedraftdue = nepa_data['statedraftdue']
			nepa.fhwadraftdue = nepa_data['fhwadraftdue']
			nepa.save()
			# raise Exception
			return home_page(request)
		else:
			## need to fix error checking
			
			return render(request, 'add.html', {'project_form' : project_form, 'nepa_form' : nepa_form})
	else:
		return render(request, 'add.html', {'project_form' : ProjectForm, 'nepa_form' : NepaForm})

def project_dash(request, projectid):
	project = get_object_or_404(Project, id=projectid)

	context = { 
				'project': project,				
			}
	return render(request, 'projectdash.html', context)

def nepa_dash(request, projectid, nepaid):
	project = get_object_or_404(Project, id=projectid)
	nepa = project.nepadocs.get(id=nepaid)
	context = { 
				'project' : project,
				'nepa': nepa,				
			}
	return render(request, 'nepadash.html', context)
	

def project_edit(request, projectid, nepaid):
	''' Should only come from edit page, so nepa should update automagically '''
	project = get_object_or_404(Project, id=projectid)
	if request.method == 'POST':
		project_form = ProjectForm(request.POST, instance=project)
		if project_form.is_valid():
			project_form.save() #save and commit job number to db			
			return redirect('project_dash', projectid=project.id)
		return render(request, 'add.html', {'project_form' : project_form})
	else:
		project_form = ProjectForm(instance=project)
		return render(request, 'add.html', {'project_form' : project_form})