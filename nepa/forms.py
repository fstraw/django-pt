from django.forms import ModelForm, Textarea, DateInput, Form
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from nepa.models import Project, PINumbers, ProjectNumbers, Nepa


class ProjectForm(ModelForm):
    class Meta:
          model = Project
          fields = ['jobnumber', 'projectname', 
                  'projectmanager', 'projectdescription',
                  'county',             'pis', 
                  'projectnumbers', 'comments']
          widgets = {
                      'comments': Textarea(attrs={'cols': 50, 'rows': 3}),
                      'projectname': Textarea(attrs={'cols': 50, 'rows': 1}),
                      'projectdescription': Textarea(attrs={'cols': 50, 'rows': 5}),
                    }

class NepaForm(ModelForm):
    class Meta:
          model = Nepa
          fields = ['project', 'specialist', 
                  'stateplanner', 'documenttype',
                  'earlycoordination', 'statedraft',
                  'statedraftdue', 'fhwadraftdue', 
                  'stateapproval', 'fhwadraft',
                  'fhwaapproval']