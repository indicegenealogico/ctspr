from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import *

# Create your views here.

#=====================================================
class HomeView(TemplateView):
  template_name = "home.html"

  def get_context_data(self, **kwargs):
    context =  super().get_context_data(**kwargs)
    return context


#=====================================================
class TownCreateView(CreateView):
  model = Town
  fields =['name', 'branch']
  success_url = reverse_lazy('home')


class TownDetailView(DetailView): 
  model = Town
  fields =['name', 'branch']


class TownUpdateView(UpdateView):
  model = Town
  fields =['name', 'branch']


class TownDeleteView(DeleteView):
  model = Town
  success_url = reverse_lazy('home')


#=====================================================
class JobCreateView(CreateView):
  model = Job
  fields = ['job_id', 'title', 'description', 'requirements', 'posting_date','closing_date', 'town', 'recruiter']
  success_url = reverse_lazy('home')
  

class JobDetailView(DetailView):
  model = Job
  fields = ['job_id', 'title', 'description', 'requirements', 'posting_date','closing_date', 'town', 'recruiter']

  
class JobUpdateView(UpdateView):
  model = Job
  fields = ['job_id', 'title', 'description', 'requirements', 'posting_date','closing_date', 'town', 'recruiter']
  

class JobDeleteView(DeleteView):
  model = Job
  success_url = reverse_lazy('home')