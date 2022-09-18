from django import forms
from django.forms import ModelForm
from . models import *




#==============================
class TownForm(forms.ModelForm):
  class Meta:
    model = Town    
    fields = ('name', 'branch')    
    labels = {
      # 'name': '',
      # 'branch': ''
    }
    
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
  closing_date   = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%m/%d/%Y', )
        )
  posting_date   = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%m/%d/%Y', )
        )

  class Meta:
    model        = Job
    fields       = '__all__'
    exclude      = ('created_date',)
    
    widgets = {
      'jobID':        forms.TextInput(attrs={'class':'form-control'}),
      'title':        forms.TextInput(attrs={'class':'form-control'}),
      # 'description':  forms.TextInput(attrs={'class':'form-control'}),
      # 'requirements': forms.MultipleChoiceField(),
      'post_date':    forms.DateField(),
      'closing_date': forms.DateField(),
      # 'town':         forms.ComboField(),
      # 'recruiter':   forms.ComboField()
    }
    
    


  