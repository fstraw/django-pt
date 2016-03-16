from django.forms import ModelForm, Textarea, DateInput, Form, TextInput
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from nepa.models import Project, PINumbers, ProjectNumbers, Nepa
from shared import PROJECT_MANAGERS


class PlannerForm(forms.Form):
    pm = forms.ChoiceField(choices=PROJECT_MANAGERS, initial='')

class ProjectForm(ModelForm):
    initial_fields = ('pinumber', 'projectnumber')
    pinumber = forms.CharField(required=False)
    projectnumber = forms.CharField(required=False)
    def __init__(self, *args, **kwargs):
      super(ProjectForm, self).__init__(*args, **kwargs)
      inst_projects = self.instance.projectnumbers.all()
      inst_pis = self.instance.pis.all()
      csv_project_numbers = [i.project_number for i in inst_projects]
      csv_pi_numbers = [i.pi_number for i in inst_pis]
      self.fields['pinumber'].initial = ','.join(csv_pi_numbers)
      self.fields['projectnumber'].initial = ','.join(csv_project_numbers)
      
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