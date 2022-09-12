from django.contrib import admin
from .models import *
from django.forms import CheckboxSelectMultiple

# Register your models here.

@admin.register(Branch)
class MakeAdmin(admin.ModelAdmin):
  list_display = ('name', 'phone', 'manager')


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
  list_display = ('name', 'branch')


@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'branch')
  ordering = ('name',)
  search_fields = ['name']


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
  ordering = ('description',)



@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
  list_display        = ('jobID', 'title', 'town')
  formfield_overrides = {
    models.ManyToManyField: {'widget': CheckboxSelectMultiple},
  }
  exclude             = ('created_date',)

