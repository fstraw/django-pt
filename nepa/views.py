from django.shortcuts import render
from django.http import HttpResponse
from nepa.forms import ProjectForm

def home_page(request):
	return render(request, 'home.html')
def add_page(request):
	return render(request, 'add.html', {'form' : ProjectForm})