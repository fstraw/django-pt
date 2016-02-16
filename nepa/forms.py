from django.forms import ModelForm, Textarea, DateInput, Form
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from nepa.models import Project, PINumbers, ProjectNumbers


# class ProjectForm(ModelForm):
# 	class Meta:
# 		model = Project
# 		fields = ['jobnumber', 'projectname', 'projectmanager', 'relatedprojects']
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

class ProjectForm(Form):      
      pis_from_db = [(pinum, pinum) for pinum in PINumbers.objects.all()]
      project_nums_from_db = [(projnum, projnum) for projnum in ProjectNumbers.objects.all()]
      projects_from_db = [(project, project) for project in Project.objects.all()]
      jobnumber = forms.CharField(max_length=15)
      projectname = forms.CharField(max_length=50)
      pinumbers = forms.MultipleChoiceField(choices=pis_from_db)
      projectnumbers = forms.MultipleChoiceField(choices=project_nums_from_db)
      projectmanager = forms.CharField(max_length=25)
      relatedprojects = forms.MultipleChoiceField(choices=projects_from_db)