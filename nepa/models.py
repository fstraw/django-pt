from django.db import models
from datetime import date
import time

# Create your models here.

## EP Project
class Project(models.Model):
	epid = models.TextField(default='')
## Related Projects and previous designations

## EP Manager
## PI Number
## GDOT Project Number
## Scope of Services
## NEPA
	nepa = models.TextField(default='')## Document Due Date
	nepa_due_date = models.DateField()
## Air
	air = models.TextField(default='')
	air_due_date = models.DateField()
## Noise
	noise = models.TextField(default='')
	noise_due_date = models.DateField()
## Ecology
	ecology = models.TextField(default='')
	ecology_due_date = models.DateField()
## Archaeology
	archaeology = models.TextField(default='')
	archaeology_due_date = models.DateField()
## History
	history = models.TextField(default='')
	history_due_date = models.DateField()
	def nepa_due_in(self):
		days = '{}'.format(self.nepa_due_date - date.today())
		days_stripped = days.replace(', 0:00:00', '')
		return days_stripped
	def air_due_in(self):
		days = '{}'.format(self.air_due_date - date.today())
		days_stripped = days.replace(', 0:00:00', '')
		return days_stripped
	def noise_due_in(self):
		days = '{}'.format(self.noise_due_date - date.today())
		days_stripped = days.replace(', 0:00:00', '')
		return days_stripped
	def ecology_due_in(self):
		days = '{}'.format(self.ecology_due_date - date.today())
		days_stripped = days.replace(', 0:00:00', '')
		return days_stripped
	def archaeology_due_in(self):
		days = '{}'.format(self.archaeology_due_date - date.today())
		days_stripped = days.replace(', 0:00:00', '')
		return days_stripped
	def history_due_in(self):
		days = '{}'.format(self.history_due_date - date.today())
		days_stripped = days.replace(', 0:00:00', '')
		return days_stripped