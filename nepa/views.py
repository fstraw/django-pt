from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
	return render(request, 'home.html')
def add_page(request):
	return render(request, 'add.html')