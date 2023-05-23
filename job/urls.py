from django.urls import path
from .views import *



urlpatterns = [
    path('createjoboffer/',CreateJobOffer.as_view()),    
    path('getplanifiedJob/',GetPlanfiedJobChallenge.as_view()),  
     path('getnonplanifiedJob/',GetNONPlanfiedJobChallenges.as_view()), 

]