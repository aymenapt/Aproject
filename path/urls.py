from django.urls import path
from .views import *



urlpatterns = [
    path('createlearningpath/',CreateLearinigPath.as_view()),
    path('creategamifiedcours/',CreateGamifiedCours.as_view()),
         
         
]