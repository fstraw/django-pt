from django.contrib import admin
from nepa.models import Project, Nepa, PINumbers, ProjectNumbers

# Register your models here.
admin.site.register(Project)
admin.site.register(Nepa)
admin.site.register(PINumbers)
admin.site.register(ProjectNumbers)