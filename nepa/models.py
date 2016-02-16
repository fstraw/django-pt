from django.db import models
from datetime import date
import time

# Create your models here.

## EP Project
class Project(models.Model):
	jobnumber = models.CharField(max_length=15, default='')
	projectname = models.CharField(max_length=50, default='')
	# projectnumber = models.CharField(max_length=18, default='')
	# pinumber = models.CharField(max_length=7, default='')
	projectmanager = models.CharField(max_length=25, default='')
	projectdescription = models.CharField(max_length=1000, default='')
	county = models.CharField(max_length=15, default='')
	relatedprojects = models.ManyToManyField('self')
	def __str__(self):
		return self.jobnumber
		
	
class Nepa(models.Model):
	project = models.ForeignKey(Project, default='')
	specialist = models.CharField(max_length=50, default='')
	stateplanner = models.CharField(max_length=50, default='')
	documenttype = models.CharField(max_length=10, default='')
	#Submittals
	earlycoordination = models.DateField()
	statedraft = models.DateField()
	stateapproval = models.DateField()
	fhwadraft = models.DateField()
	fhwaapproval = models.DateField()
	#Due Dates
	statedraftdue = models.DateField()
	fhwadraftdue = models.DateField()
	def statedraft_due_in(self):
		days = '{}'.format(self.statedraftdue - date.today())
		days_stripped = days.replace(', 0:00:00', '')
		return days_stripped
	def fhwadraft_due_in(self):
		days = '{}'.format(fhwadatedue - date.today())
		days_stripped = days.replace(', 0:00:00', '')
		return days_stripped
	# def __str__(self):
	# 	return self.jobnumber

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

class PINumbers(models.Model):    
    project = models.ForeignKey(Project)
    pi_number = models.CharField(max_length=7, null=True)
    
    class Meta:
            verbose_name_plural = 'PI Numbers'
    def __str__(self):
        return self.pi_number
        
class ProjectNumbers(models.Model):
    project = models.ForeignKey(Project)
    project_number = models.CharField(max_length=20, blank=True, null=True)
    
    class Meta:
            verbose_name_plural = 'Project Numbers'
    def __str__(self):
        return self.project_number