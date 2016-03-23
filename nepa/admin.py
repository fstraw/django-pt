from django.contrib import admin
import nepa.models

## Register your models here.

admin.site.register(nepa.models.Project)
admin.site.register(nepa.models.ProjectNumbers)
admin.site.register(nepa.models.PINumbers)
admin.site.register(nepa.models.Nepa)
admin.site.register(nepa.models.Air)
admin.site.register(nepa.models.Noise)
admin.site.register(nepa.models.Ecology)
admin.site.register(nepa.models.Aquatics)
admin.site.register(nepa.models.Archaeology)
admin.site.register(nepa.models.History)