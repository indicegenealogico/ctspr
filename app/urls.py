from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path(''          , HomeView.as_view()       , name='home'),
    path('contact/'  , ContactView.as_view()    , name='contact'),
    path('login/'    , views.login              , name='login'),

    # path('town/'               , TownListView.as_view()),
    path('town/add'            , TownCreateView.as_view(), name='town_add'),
    path('town/<int:pk>/detail', TownDetailView.as_view(), name='town_detail'),
    path('town/<int:pk>/update', TownUpdateView.as_view(), name='town_update'),
    path('town/<int:pk>/delete', TownDeleteView.as_view(), name='town_delete'),
    
    path('job/add'             , JobCreateView.as_view(), name='job_add'),
    path('job/<int:pk>/detail' , JobDetailView.as_view(), name='job_detail'),
    path('job/<int:pk>/update' , JobUpdateView.as_view(), name='job_update'),
    path('job/<int:pk>/delete' , JobDeleteView.as_view(), name='job_delete'),
    
    path('jobs/<str>/ofertas'  , BranchJobsView.as_view(), name='branch_jobs'),
    path('jobs/ofertas'        , AllJobsView.as_view()   , name='ofertas'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)