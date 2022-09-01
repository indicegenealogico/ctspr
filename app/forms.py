from django import forms
from django.forms import ModelForm
from . models import *
from django.conf import settings



#==============================
class TownForm(ModelForm):
  class Meta:
    model = Town
    
    fields = ('name', 'branch')
    
    labels = {
      # 'name': '',
      # 'branch': ''
    }
    
    widgets = {
      'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the Town Name'}),
      'branch': forms.Select(attrs={'class':'form-control', 'placeholder':'Enter the Town Name'})
    }


#==============================
class RecruiterForm(ModelForm):
  class Meta:
    model  = Recruiter
    fields = "__all__"
    
    
#==============================
class JobForm(ModelForm):
  class Meta:
    model        = Job
    fields       = '__all__'
    exclude      = ('created_date',)
    requirements = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple)
    posting_date = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%m/%d/%Y', )
        )