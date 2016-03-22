from django.db import models
from django.utils import timezone
from datetime import date
from shared import NEPA_PLANNERS, PROJECT_MANAGERS, COUNTY_NAMES, DOCUMENT_TYPES, COUNTIES, DEPARTMENTS, EMPLOYEES, ENVIRONMENTAL_DOCUMENTS

# Create your models here.
## EP Project
class Project(models.Model):
	jobnumber = models.CharField(max_length=15, default='', unique=True)
	projectname = models.CharField(max_length=50, default='')
	projectmanager = models.CharField(max_length=25, default='', choices=PROJECT_MANAGERS)
	projectdescription = models.CharField(max_length=1000, default='')
	client = models.CharField(max_length=30, default='', blank=True)
	county = models.CharField(max_length=15, default='', choices=COUNTY_NAMES)
	# relatedprojects = models.ManyToManyField('self', null=True)
	comments = models.CharField(max_length=1000, default='', blank=True)
	def gdot_district(self):
		if self.county:
			return '{}'.format(COUNTIES[self.county])
		else:
			return 'Unassigned'
	def __str__(self):
		return self.jobnumber

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

class SpecialStudy(models.Model):
	""" Base class for special studies documents """
	project = models.ForeignKey(Project, default='')
	specialist = models.CharField(max_length=50, default='', choices=EMPLOYEES)
	documenttype = models.CharField(max_length=10, default='', choices=DOCUMENT_TYPES)
	draftsubmittal = models.DateField(null=True, blank=True)
	draftapproval = models.DateField(null=True, blank=True)
	duedate = models.DateField(null=True, blank=True)
	class Meta:
		abstract = True
	def __str__(self):
		# return '{}_{}'.format(self.project.jobnumber, self.documenttype)
		return '{}'.format(self.documenttype)

class Nepa(models.Model):
	project = models.ForeignKey(Project, default='')
	specialist = models.CharField(max_length=50, default='', choices=NEPA_PLANNERS)
	stateplanner = models.CharField(max_length=50, default='')
	documenttype = models.CharField(max_length=15, default='', choices=ENVIRONMENTAL_DOCUMENTS)
	#Submittals
	earlycoordination = models.DateField(null=True, blank=True)
	statedraft = models.DateField(null=True, blank=True)
	stateapproval = models.DateField(null=True, blank=True)
	fhwadraft = models.DateField(null=True, blank=True)
	fhwaapproval = models.DateField(null=True, blank=True)
	#Due Dates
	statedraftdue = models.DateField(null=True, blank=True)
	fhwadraftdue = models.DateField(null=True, blank=True)
	def statedraft_due_in(self):
		if self.stateapproval:
			return 'Approved'
		if self.statedraftdue:
			date_diff = self.statedraftdue - date.today()
			if not date_diff:
				return 'Due Today'
			days = '{}'.format(date_diff)
			days_stripped = days.replace(', 0:00:00', '')
			return days_stripped
		return 'No Date'
	def fhwadraft_due_in(self):
		if self.fhwaapproval:
			return 'Approved'
		if self.fhwadraftdue:
			date_diff = self.fhwadraftdue - date.today()
			if not date_diff:
				return 'Due Today'
			days = '{}'.format(self.fhwadraftdue - date.today())
			days_stripped = days.replace(', 0:00:00', '')
			return days_stripped
		return 'No Date'
	def __str__(self):
		# return '{}_{}'.format(self.project.jobnumber, self.documenttype)
		return '{}'.format(self.documenttype)

class Air(SpecialStudy):
	pass

class Noise(SpecialStudy):
	pass

class Ecology(SpecialStudy):
	pass

class Aquatics(SpecialStudy):
	pass

class Archaeology(SpecialStudy):
	pass

class History(SpecialStudy):
	pass