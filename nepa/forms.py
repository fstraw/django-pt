from django.forms import ModelForm, Textarea, DateInput, Form, TextInput, CharField, ChoiceField
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from nepa.models import Project, PINumbers, ProjectNumbers, Nepa, Air
from shared import PROJECT_MANAGERS, ENVIRONMENTAL_DOCUMENTS, NEPA_PLANNERS


class PlannerForm(forms.Form):
    pm = forms.ChoiceField(choices=PROJECT_MANAGERS, initial='')

class ProjectForm(ModelForm):
    initial_fields = ('pinumber', 'projectnumber')
    pinumber = forms.CharField(required=False, label='PI Number(s)')
    projectnumber = forms.CharField(required=False, label='Project Number(s)')
    def __init__(self, *args, **kwargs):
      super(ProjectForm, self).__init__(*args, **kwargs)
      try:
        inst_projects = self.instance.projectnumbers.all()
      except:
        inst_projects = []
      try:
        inst_pis = self.instance.pis.all()
      except:
        inst_pis = []
      ##Create initial form values from database values
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
      labels = {
            'jobnumber': _('Job Number'),
			'projectname': _('Project Name'),
			'projectmanager': _('Project Manager'),
			'projectdescription': _('Project Description'),
        }

class NepaForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(NepaForm, self).__init__(*args, **kwargs)
    self.fields['documenttype'].choices = ENVIRONMENTAL_DOCUMENTS
    self.fields['specialist'].choices = NEPA_PLANNERS
  class Meta:          
    model = Nepa
    fields = ['project', 'specialist', 
                  'stateplanner', 'documenttype',                  
                  'statedraftdue', 'fhwadraftdue',
				          'earlycoordination', 'statedraft',
                  'stateapproval', 'fhwadraft',
                  'fhwaapproval']
    widgets = {
        'earlycoordination': DateInput(attrs={'class':'datepicker'}),
				'statedraft': DateInput(attrs={'class':'datepicker'}),
				'statedraftdue': DateInput(attrs={'class':'datepicker'}),
				'fhwadraftdue': DateInput(attrs={'class':'datepicker'}),
				'stateapproval': DateInput(attrs={'class':'datepicker'}),
				'fhwadraft': DateInput(attrs={'class':'datepicker'}),
				'fhwaapproval': DateInput(attrs={'class':'datepicker'}),
        }
    labels = {
			'stateplanner':_('State Planner'),
      'earlycoordination': _('Early Coordination On'),
      'documenttype': _('Document Type'),
			'statedraft': _('State Draft Submitted On'),
			'statedraftdue': _('State Draft Due'),
			'fhwadraftdue': _('FHWA Draft Due'),
			'stateapproval': _('State Approval'),
			'fhwadraft': _('FHWA Draft Submitted On'),
			'fhwaapproval': _('FHWA Approval'),
        }

class AirForm(ModelForm):
  # def __init__(self, *args, **kwargs):
  #   super(AirForm, self).__init__(*args, **kwargs)
  #   self.fields['documenttype'].choices = AIR_DOCUMENT_TYPES
  class Meta:
    model = Air
    fields = ['project', 'documenttype', 'specialist','draftsubmittal', 
              'draftapproval', 'duedate']
    widgets = {
        'draftsubmittal': DateInput(attrs={'class':'datepicker'}),
        'draftapproval': DateInput(attrs={'class':'datepicker'}),
        'duedate': DateInput(attrs={'class':'datepicker'}),
        }

    labels = {
      'draftsubmittal':_('Draft Submittal'),
      'draftapproval': _('Draft Approval'),
      'duedate': _('Due Date'),
      }