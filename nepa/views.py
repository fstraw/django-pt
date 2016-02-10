from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from nepa.forms import ProjectForm
from nepa.models import Project

def home_page(request):
	project_list = Project.objects.all()
	context = RequestContext(request, {'project_list' : project_list})
	template = loader.get_template('home.html')
	return HttpResponse(template.render(context))
	# return render(request, 'home.html', context)
def add_page(request):
	if request.method == 'POST':		
		form = ProjectForm(request.POST)
		if form.is_valid():
			form.save()
			return home_page(request)  
		else:
			## need to fix error checking
			return render(request, 'add.html', {'form' : ProjectForm})
	else:
		return render(request, 'add.html', {'form' : ProjectForm})