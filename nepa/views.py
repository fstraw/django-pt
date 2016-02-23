from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from nepa.forms import ProjectForm, NepaForm
from nepa.models import Project, Nepa, ProjectNumbers, PINumbers

def home_page(request):
	project_list = Project.objects.all()
	# nepas = Project.objects.all()[1].nepa_set
	context = RequestContext(request, {'project_list' : project_list,
										})
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

	context = { 'project': project,
				# 'jobnumber' : project.jobnumber, 
				# 'projectname' : project.projectname,
				# 'projectdescription' : project.projectdescription,				
				# 'projectnumbers' : project.projectnumbers,
				# 'projectmanager' : project.projectmanager,
				# 'county' : project.county,				
				}
	return render(request, 'projectdash.html', context)

def project_edit(request, projectid):
	''' Should only come from edit page, so nepa should update automagically '''
	project = get_object_or_404(Project, id=projectid)
	nepa = project.nepa_set.all()[0]
	if request.method == 'POST':
		project_form = ProjectForm(request.POST, instance=project)
		nepa_form = NepaForm(request.POST, instance=nepa) #should only be one nepa project if Foreign Key is used
		if project_form.is_valid():
			project_form.save() #save and commit job number to db, should update nepa automagically				
			nepa_form.save()
			return redirect('project_dash', projectid=project.id)
		return render(request, 'add.html', {'project_form' : project_form, 'nepa_form' : nepa_form})
	else:
		project_form = ProjectForm(instance=project)
		nepa_form = NepaForm(instance=project.nepa_set.all()[0])
		return render(request, 'add.html', {'project_form' : project_form, 'nepa_form' : nepa_form})