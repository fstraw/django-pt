from django.db import models
from datetime import date
import time

# Create your models here.

## EP Project
class Project(models.Model):
	jobnumber = models.CharField(max_length=15, default='')
	projectname = models.CharField(max_length=50, default='')
	projectnumber = models.CharField(max_length=18, default='')
	pinumber = models.CharField(max_length=7, default='')
	projectmanager = models.CharField(max_length=25, default='')
	projectdescription = models.CharField(max_length=1000, default='')
	county = models.CharField(max_length=15, default='')
	relatedprojects = models.ManyToManyField('self')
	def __str__(self):
		return self.jobnumber
		
	
class Nepa(models.Model):
	jobnumber = models.ForeignKey(Project, default='')
	specialist = models.CharField(max_length=50, default='')
	stateplanner = models.CharField(max_length=50, default='')
	documenttype = models.CharField(max_length=10, default='')
	earlycoordination = models.DateField()
	statedraft = models.DateField()
	stateapproval = models.DateField()
	fhwadraft = models.DateField()
	fhwaapproval = models.DateField()

class Air(models.Model):
	pass

class Noise(models.Model):
	pass

class Ecology(models.Model):
	pass

class Aquatics(models.Model):
	pass

class Archaeology(models.Model):
	pass

class History(models.Model):
	pass