from django import forms
from django.forms import ModelForm
from . models import *




#==============================
class TownForm(forms.ModelForm):
  
  class Meta:
    model = Town    
    fields = ('name', 'branch')    
    
    widgets = {
      'name'  : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the Town Name'}),
      'branch': forms.Select(attrs={'class':'form-control', 'placeholder':'Enter the Town Name'})
    }


#==============================
class RecruiterForm(forms.ModelForm):
  class Meta:
    model  = Recruiter
    fields = "__all__"
    
    
#==============================
class JobForm(forms.ModelForm):

  class Meta:
    model        = Job
    fields       = '__all__'
    exclude      = ('created_date',)
    
    widgets = {
      'jobID'       : forms.TextInput(attrs={'class':'form-control'}),
      'title'       : forms.TextInput(attrs={'class':'form-control'}),
      'description' : forms.Textarea(attrs={'class':'form-control'}),
      'requirements': forms.CheckboxSelectMultiple(),
      'posting_date': forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker form-control'}),      
      'closing_date': forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker form-control'}),
      'town'        : forms.Select(attrs={'class': 'form-control'}),
      'recruiter'   : forms.Select(attrs={'class': 'form-control'}),
    }
    
    


  