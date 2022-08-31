from django import forms
from django.forms import ModelForm
from . models import *


class TownForm(ModelForm):
  class Meta:
    model = Town
    # fields = "__all__"
    fields = ('name', 'branch')

    labels = {
      'name': '',
      'branch': ''
    }

    widgets = {
      'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the Town Name'}),
      'branch': forms.Select(attrs={'class':'form-control', 'placeholder':'Enter the Town Name'})
    }