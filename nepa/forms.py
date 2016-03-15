from django.forms import ModelForm, Textarea, DateInput, Form, TextInput
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from nepa.models import Project, PINumbers, ProjectNumbers, Nepa
from shared import PROJECT_MANAGERS


class PlannerForm(forms.Form):

    pm = forms.ChoiceField(choices=PROJECT_MANAGERS, initial='')

class ProjectForm(ModelForm):
    class Meta:
          model = Project
          fields = ['jobnumber', 'projectname', 'client',
                  'projectmanager', 'projectdescription',
                  'county', 'comments']
          widgets = {
                      'jobnumber': Textarea(attrs={'cols': 20, 'rows': 1}),
                      'projectname': Textarea(attrs={'cols': 40, 'rows': 1}),
					  'client': Textarea(attrs={'cols': 40, 'rows': 1}),
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
    widgets = {'earlycoordination': DateInput(attrs={'class':'datepicker'}),
				'statedraft': DateInput(attrs={'class':'datepicker'}),
				'statedraftdue': DateInput(attrs={'class':'datepicker'}),
				'fhwadraftdue': DateInput(attrs={'class':'datepicker'}),
				'stateapproval': DateInput(attrs={'class':'datepicker'}),
				'fhwadraft': DateInput(attrs={'class':'datepicker'}),
				'fhwaapproval': DateInput(attrs={'class':'datepicker'}),}