from django.contrib import admin
from .models import *
from django.forms import CheckboxSelectMultiple

# Register your models here.

@admin.register(Branch)
class MakeAdmin(admin.ModelAdmin):
  list_display = ('name', 'phone', 'manager')


@admin.register(Town)
class MakeAdmin(admin.ModelAdmin):
  list_display = ('name', 'branch')


@admin.register(Recruiter)
class MakeAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'branch')

@admin.register(Requirement)
class MakeAdmin(admin.ModelAdmin):
  pass


@admin.register(Job)
class MakeAdmin(admin.ModelAdmin):
  list_display = ('job_id', 'title', 'town')


class RequirementAdmin(admin.ModelAdmin):
  formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
  pass