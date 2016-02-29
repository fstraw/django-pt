from django.db import models
from django.utils import timezone
from datetime import date
from shared import NEPA_PLANNERS, PROJECT_MANAGERS, COUNTY_NAMES, DOCUMENT_TYPES

# Create your models here.

## EP Project
class Project(models.Model):
	jobnumber = models.CharField(max_length=15, default='', unique=True)
	projectname = models.CharField(max_length=50, default='')
	projectmanager = models.CharField(max_length=25, default='', choices=PROJECT_MANAGERS)
	projectdescription = models.CharField(max_length=1000, default='')
	county = models.CharField(max_length=15, default='', choices=COUNTY_NAMES)
	# relatedprojects = models.ManyToManyField('self', null=True)
	comments = models.CharField(max_length=1000, default='', blank=True)
	def __str__(self):
		return self.jobnumber		
	
class Nepa(models.Model):
	project = models.ForeignKey(Project, default='', related_name='nepadocs')
	specialist = models.CharField(max_length=50, default='', choices=NEPA_PLANNERS)
	stateplanner = models.CharField(max_length=50, default='')
	documenttype = models.CharField(max_length=10, default='', choices=DOCUMENT_TYPES)
	#Submittals
	earlycoordination = models.DateField(default=timezone.now)
	statedraft = models.DateField(default=timezone.now)
	stateapproval = models.DateField(default=timezone.now)
	fhwadraft = models.DateField(default=timezone.now)
	fhwaapproval = models.DateField(default=timezone.now)
	#Due Dates
	statedraftdue = models.DateField(default=timezone.now)
	fhwadraftdue = models.DateField(default=timezone.now)
	def statedraft_due_in(self):
		if self.statedraftdue:
			date_diff = self.statedraftdue - date.today()
			if not date_diff:
				return 'Due Today'
			days = '{}'.format(date_diff)
			days_stripped = days.replace(', 0:00:00', '')
			return days_stripped
		return 'No Date'
	def fhwadraft_due_in(self):
		if self.fhwadraftdue:
			date_diff = self.fhwadraftdue - date.today()
			if not date_diff:
				return 'Due Today'
			days = '{}'.format(self.fhwadraftdue - date.today())
			days_stripped = days.replace(', 0:00:00', '')
			return days_stripped
		return 'No Date'
	def __str__(self):
		return '{}_{}'.format(self.project.jobnumber, self.documenttype)

class Air(models.Model):
	project = models.ForeignKey(Project, default='')
	specialist = models.CharField(max_length=50, default='')
	##doc type (PM2.5, air assessment, memorandum)
	documenttype = models.CharField(max_length=10, default='')
	rptdeadline = models.DateField(default=timezone.now)
	pmsubmitted = models.DateField(default=timezone.now)
	pmapproval = models.DateField(default=timezone.now)
	rptsubmittal = models.DateField(default=timezone.now)
	rptapproval = models.DateField(default=timezone.now)
	comments = models.CharField(max_length=1000, default='', blank=True)
	def __str__(self):
		return self.project.jobnumber
class Noise(models.Model):
	project = models.ForeignKey(Project, default='')
	specialist = models.CharField(max_length=50, default='')
	documenttype = models.CharField(max_length=10, default='')

class Ecology(models.Model):
	project = models.ForeignKey(Project, default='')
	specialist = models.CharField(max_length=50, default='')
	documenttype = models.CharField(max_length=10, default='')

class Aquatics(models.Model):
	project = models.ForeignKey(Project, default='')
	specialist = models.CharField(max_length=50, default='')
	documenttype = models.CharField(max_length=10, default='')

class Archaeology(models.Model):
	project = models.ForeignKey(Project, default='')
	specialist = models.CharField(max_length=50, default='')
	documenttype = models.CharField(max_length=10, default='')

class History(models.Model):
	project = models.ForeignKey(Project, default='')
	specialist = models.CharField(max_length=50, default='')
	documenttype = models.CharField(max_length=10, default='')

class PINumbers(models.Model):
    projects = models.ManyToManyField(Project, related_name='pis')
    pi_number = models.CharField(max_length=7, null=True, unique=True)
    class Meta:
            verbose_name_plural = 'PI Numbers'
    def __str__(self):
        return self.pi_number
        
class ProjectNumbers(models.Model):
    projects = models.ManyToManyField(Project, related_name='projectnumbers')
    project_number = models.CharField(max_length=20, null=True, unique=True)    
    class Meta:
            verbose_name_plural = 'Project Numbers'
    def __str__(self):
        return self.project_number