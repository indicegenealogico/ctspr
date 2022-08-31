from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from app.models import Town

# Create your views here.

class HomeView(TemplateView):
  
  template_name = "home.html"

  def get_context_data(self, **kwargs):
    context =  super().get_context_data(**kwargs)
    return context


class TownDetailView(DetailView):
  
  model = Town

  def get_context_data(self, **kwargs):
    context =  super().get_context_data(**kwargs)
    context['towns'] = Town.objects.all()
    return context


class TownListView(ListView):
  
  model = Town
  paginate_by = 15

  def get_context_data(self, **kwargs):
    context =  super().get_context_data(**kwargs)
    return context





#=====================================================================
#Agregar un form
from . forms import *
from django.shortcuts import render
from django.http import HttpResponseRedirect

def add_town(request):
  submitted = False
  if request.method == 'POST':
    form = TownForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/add_town?submitted=True')
  else:
    form = TownForm
    if 'submitted' in request.GET:
      submitted = True
  
  return render(request, 'app/add_town.html', {'form':form, 'submitted':submitted})
