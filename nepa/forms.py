from django.forms import ModelForm
from nepa.models import Projects

class ProjectForm(ModelForm):
	class Meta:
		model = Projects
		fields = ['epid', 'air', 'noise', 'ecology', 'archaeology', 'history']