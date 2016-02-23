from django.forms import ModelForm, Textarea, DateInput, Form, TextInput
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from nepa.models import Project, PINumbers, ProjectNumbers, Nepa


class ProjectForm(ModelForm):
    class Meta:
          model = Project
          fields = ['jobnumber', 'projectname', 
                  'projectmanager', 'projectdescription',
                  'county', 'comments']
          widgets = {
                      'jobnumber': Textarea(attrs={'cols': 20, 'rows': 1}),
                      'projectname': Textarea(attrs={'cols': 40, 'rows': 1}),
                      'projectdescription': Textarea(attrs={'cols': 50, 'rows': 3}),
                      'comments': Textarea(attrs={'cols': 50, 'rows': 3}),
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
    # widgets = {'project': TextInput(attrs={'readonly':'readonly'})}