from django.db import models

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
	## Document Due Date
## Air
	air = models.TextField(default='')
	## Document Due Date
## Noise
	noise = models.TextField(default='')
	## Document Due Date
## Ecology
	ecology = models.TextField(default='')
	##Document Due Date
## Archaeology
	archaeology = models.TextField(default='')
	##Document Due Date
## History
	history = models.TextField(default='')
	##Document Due Date