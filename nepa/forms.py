from django.forms import ModelForm, Textarea, DateInput, Form
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from nepa.models import Project, PINumbers, ProjectNumbers, Nepa


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

# class ProjectForm(Form):      
#       jobnumber = forms.CharField(max_length=15)
#       projectname = forms.CharField(max_length=50)
#       projectmanager = forms.CharField(max_length=25)
#       projectdescription = forms.CharField(max_length=1000)
#       county = forms.CharField(max_length=25)
#       pis = forms.ModelMultipleChoiceField(queryset=PINumbers.objects.all())
#       projectnumbers = forms.ModelMultipleChoiceField(queryset=ProjectNumbers.objects.all())
#       comments = forms.CharField(max_length=1000)
      # relatedprojects = forms.ModelMultipleChoiceField(queryset=Project.objects.all())


class ProjectForm(ModelForm):
    class Meta:
          model = Project
          fields = ['jobnumber', 'projectname', 
                  'projectmanager', 'projectdescription',
                  'county',             'pis', 
                  'projectnumbers', 'comments']
          widgets = {'comments': Textarea(attrs={'cols': 20, 'rows': 3})}

class NepaForm(ModelForm):
    class Meta:
          model = Nepa
          fields = ['project', 'specialist', 
                  'stateplanner', 'documenttype',
                  'earlycoordination', 'statedraft',
                  'statedraftdue', 'fhwadraftdue', 
                  'stateapproval', 'fhwadraft',
                  'fhwaapproval']