from django.urls import path
from app.views import *
from . import views

urlpatterns = [
    path(''          , HomeView.as_view()      , name='home'),
    path('town/<pk>/', TownDetailView.as_view(), name='town_detail'),
    path('town/list/', TownListView.as_view()  , name='town_list'),
    path('town/add_new', views.add_town, name='add_town'),

]