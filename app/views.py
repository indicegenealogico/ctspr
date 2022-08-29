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


from app.forms import *
from django.views.generic.edit import FormView

class BranchFormView(FormView):
    template_name = 'branch.html'
    form_class = BranchForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)