from django.forms import ModelForm, Textarea
from nepa.models import Project

class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = ['epid', 'air', 'noise', 'ecology', 'archaeology', 'history']
		widgets = {
            'epid': Textarea(attrs={'cols': 20, 'rows': 1}),
            'air': Textarea(attrs={'cols': 20, 'rows': 1}),
            'noise': Textarea(attrs={'cols': 20, 'rows': 1}),
            'ecology': Textarea(attrs={'cols': 20, 'rows': 1}),
            'archaeology': Textarea(attrs={'cols': 20, 'rows': 1}),
            'history': Textarea(attrs={'cols': 20, 'rows': 1}),
        }