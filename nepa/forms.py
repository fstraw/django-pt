from django.forms import ModelForm, Textarea, DateInput
from django.forms.extras.widgets import SelectDateWidget
from nepa.models import Project
from django.contrib.admin.widgets import AdminDateWidget

class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = ['jobnumber', 'projectname', 'projectnumber', 'pinumber', 
					'projectmanager']
		# widgets = {	
            # 'epid': Textarea(attrs={'cols': 20, 'rows': 1}),
            # 'air': Textarea(attrs={'cols': 20, 'rows': 1}),
            # 'noise': Textarea(attrs={'cols': 20, 'rows': 1}),
            # 'ecology': Textarea(attrs={'cols': 20, 'rows': 1}),
            # 'archaeology': Textarea(attrs={'cols': 20, 'rows': 1}),
            # 'history': Textarea(attrs={'cols': 20, 'rows': 1}),
            # 'nepa_due_date': SelectDateWidget(),
            # 'air_due_date': SelectDateWidget(),
            # 'noise_due_date': SelectDateWidget(),
            # 'ecology_due_date': SelectDateWidget(),
            # 'archaeology_due_date': SelectDateWidget(),
            # 'history_due_date': SelectDateWidget(),

        # }