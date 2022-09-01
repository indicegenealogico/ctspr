from django.urls import path
from app.views import *
from . import views

urlpatterns = [
    path(''          , HomeView.as_view()      , name='home'),

    # path('town/'               , TownListView.as_view()),
    path('town/add'            , TownCreateView.as_view(), name='town_add'),
    path('town/<int:pk>/detail', TownDetailView.as_view(), name='town_detail'),
    path('town/<int:pk>/update', TownUpdateView.as_view(), name='town_update'),
    path('town/<int:pk>/delete', TownDeleteView.as_view(), name='town_delete'),
    
    path('job/add'             , JobCreateView.as_view(), name='job_add'),
    path('job/<int:pk>/detail' , JobDetailView.as_view(), name='job_add'),
    path('job/<int:pk>/update' , JobUpdateView.as_view(), name='job_add'),
    path('job/<int:pk>/delete' , JobDeleteView.as_view(), name='job_add'),

]