from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *



from django.shortcuts import render


# Create your views here.
#=====================================================
class HomeView(TemplateView):
  template_name = "home.html"

  def get_context_data(self):
    branches  = Branch.objects.all()
    # towns     = Town.objects.all()

    towns = Town.objects.raw(''' SELECT app_branch.id, app_branch.name AS br, app_town.name AS tw
                                  FROM (app_town INNER JOIN app_job ON app_town.id = app_job.town_id) 
                                  INNER JOIN app_branch ON app_town.branch_id = app_branch.id
                                  GROUP BY app_branch.id, app_town.name
                            ''')
    context   = {'branches':branches, 'towns':towns}
    return context


#=====================================================
class ContactView(TemplateView):
  template_name = "contact.html"

  
  
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
  form_class = JobForm
  # fields = ['jobID', 'title', 'description', 'requirements', 'posting_date','closing_date', 'town', 'recruiter']
  success_url = reverse_lazy('home')
  

class JobDetailView(TemplateView):
  template_name= 'app/job_detail.html'
  
  def get_context_data(self, pk):
    job     = Job.objects.get(id=pk)
    reqs    = Requirement.objects.filter(job=job.id)
    town    = Town.objects.get(id=job.town_id)
    branch  = Branch.objects.get(id=town.branch_id)
    context = {'branch':branch, 'job':job, 'reqs':reqs }
    return context
  

class JobUpdateView(UpdateView):
  model = Job
  fields = ['job_id', 'title', 'description', 'requirements', 'posting_date','closing_date', 'town', 'recruiter']
  

class JobDeleteView(DeleteView):
  model = Job
  success_url = reverse_lazy('home')
  

  

#=====================================================
def login(request):
  return render(request, 'login.html', {})



#=====================================================
class BranchJobsView(TemplateView):
  template_name = 'app/branch_jobs.html'
  
  def get_context_data(self, branch_code="SA"):
    branch = Branch.objects.get(name=branch_code)
    jobs   = Job.objects.raw('''SELECT app_branch.name AS suc, app_town.name AS pueblo, app_job.jobID, app_job.title, app_job.id 
                              FROM app_branch INNER JOIN app_town ON app_branch.id = app_town.branch_id INNER JOIN app_job ON app_town.id = app_job.town_id
                              WHERE app_branch.name = %s
                              ORDER BY app_town.name, app_job.title ''', [branch_code])
    context = {'branch':branch, 'jobs':jobs}
    return context



#=====================================================
class AllJobsView(TemplateView):
  template_name = 'app/all_jobs.html'
  
  def get_context_data(self):
    jobs   = Job.objects.raw('''SELECT app_branch.name AS suc, app_town.name AS pueblo, app_job.jobID, app_job.title, app_job.id 
                              FROM app_branch INNER JOIN app_town ON app_branch.id = app_town.branch_id INNER JOIN app_job ON app_town.id = app_job.town_id
                              ORDER BY app_town.name, app_job.title ''')
    context = {'jobs':jobs}
    return context


#=====================================================
class TownJobsView(TemplateView):
  template_name = 'app/town_jobs.html'
  
  def get_context_data(self, branch_code='', city=''):
    branch = Branch.objects.get(name=branch_code)
    jobs   = Job.objects.raw('''SELECT app_branch.name AS suc, app_town.name AS pueblo, app_job.jobID, app_job.title, app_job.id 
                              FROM app_branch INNER JOIN app_town ON app_branch.id = app_town.branch_id INNER JOIN app_job ON app_town.id = app_job.town_id
                              WHERE app_town.name = %s
                              ORDER BY app_town.name, app_job.title ''', [city])
    context = {'branch':branch, 'jobs':jobs, 'city':city}
    return context