from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from nepa.forms import ProjectForm
from nepa.models import Project, Nepa, ProjectNumbers, PINumbers

def home_page(request):
	project_list = Project.objects.all()
	context = RequestContext(request, {'project_list' : project_list})
	template = loader.get_template('home.html')
	return HttpResponse(template.render(context))

def add_page(request):
	if request.method == 'POST':		
		form = ProjectForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
			# return home_page(request)
		else:
			## need to fix error checking
			return render(request, 'add.html', {'form' : ProjectForm})
	else:
		return render(request, 'add.html', {'form' : ProjectForm})

def project_dash(request, projectid):
	project = Project.objects.get(id=projectid)
	try:
		nepa = Nepa.objects.get(project=project)
		specialist = nepa.specialist
		stateplanner = nepa.stateplanner
		documenttype = nepa.documenttype
		earlycoordination = nepa.earlycoordination
		statedraft = nepa.statedraft
		stateapproval = nepa.stateapproval
		fhwadraft = nepa.fhwadraft
		fhwaapproval = nepa.fhwaapproval
	except:
		specialist = 'Unnassigned'
		stateplanner = 'Unassigned'
		documenttype = 'No Document Type'
		earlycoordination = 'No Early Coordination Date'
		statedraft = 'No State Draft Date'
		stateapproval = 'No State Approval Date'
		fhwadraft = 'No FHWA Draft Date'
		fhwaapproval = 'No FHWA Approval Date'
	context = {'jobnumber' : project.jobnumber, 
				'projectname' : project.projectname,
				'projectdescription' : project.projectdescription,
				# 'pinumber' : project.pinumber,
				# 'projectnumber' : project.projectnumber,
				'projectmanager' : project.projectmanager,
				'county' : project.county,
				'specialist' : specialist,
				'stateplanner' : stateplanner,
				'documenttype' : documenttype,
				'earlycoordination' : earlycoordination,
				'statedraft' : statedraft,
				'stateapproval' : stateapproval,
				'fhwadraft' : fhwadraft,
				'fhwaapproval' : fhwaapproval,
				}
	return render(request, 'projectdash.html', context)