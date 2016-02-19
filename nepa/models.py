from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.

## EP Project
class Project(models.Model):
	jobnumber = models.CharField(max_length=15, default='', unique=True)
	projectname = models.CharField(max_length=50, default='')
	projectmanager = models.CharField(max_length=25, default='')
	projectdescription = models.CharField(max_length=1000, default='')
	county = models.CharField(max_length=15, default='')
	# relatedprojects = models.ManyToManyField('self', null=True)
	pis = models.ManyToManyField('PINumbers', related_name='pinumbers')
	projectnumbers = models.ManyToManyField('ProjectNumbers', related_name='projectnumbers')
	comments = models.CharField(max_length=1000, default='', blank=True)
	def __str__(self):
		return self.jobnumber		
	
class Nepa(models.Model):
	project = models.ForeignKey(Project, default='')
	specialist = models.CharField(max_length=50, default='')
	stateplanner = models.CharField(max_length=50, default='')
	documenttype = models.CharField(max_length=10, default='')
	#Submittals
	earlycoordination = models.DateField(default=timezone.now())
	statedraft = models.DateField(default=timezone.now())
	stateapproval = models.DateField(default=timezone.now())
	fhwadraft = models.DateField(default=timezone.now())
	fhwaapproval = models.DateField(default=timezone.now())
	#Due Dates
	statedraftdue = models.DateField(default=timezone.now())
	fhwadraftdue = models.DateField(default=timezone.now())
	def statedraft_due_in(self):
		days = '{}'.format(self.statedraftdue - date.today())
		days_stripped = days.replace(', 0:00:00', '')
		return days_stripped
	def fhwadraft_due_in(self):
		days = '{}'.format(self.fhwadraftdue - date.today())
		days_stripped = days.replace(', 0:00:00', '')
		return days_stripped
	def __str__(self):
		return '{}_Nepa'.format(self.project.jobnumber)

class Air(models.Model):
	project = models.ForeignKey(Project, default='')
	specialist = models.CharField(max_length=50, default='')
	##doc type (PM2.5, air assessment, memorandum)
	documenttype = models.CharField(max_length=10, default='')
	rptdeadline = models.DateField(default=timezone.now())
	pmsubmitted = models.DateField(default=timezone.now())
	pmapproval = models.DateField(default=timezone.now())
	rptsubmittal = models.DateField(default=timezone.now())
	rptapproval = models.DateField(default=timezone.now())
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
    pi_number = models.CharField(max_length=7, null=True, unique=True)
    class Meta:
            verbose_name_plural = 'PI Numbers'
    def __str__(self):
        return self.pi_number
        
class ProjectNumbers(models.Model):
    project_number = models.CharField(max_length=20, null=True, unique=True)    
    class Meta:
            verbose_name_plural = 'Project Numbers'
    def __str__(self):
        return self.project_number