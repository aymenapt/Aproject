from django.urls import path
from .views import *



urlpatterns = [
    path('createlearningpath/',CreateLearinigPath.as_view()),
    path('creategamifiedcours/',CreateGamifiedCours.as_view()),
    path('deleteupdategamifycours/<int:id>/',GamifiedCoursUpdateDelete.as_view(),), 
    path('deleteupdatelearnpath/<int:id>/',LearnPathUpdateDelete.as_view(),), 

    path('participateoncours/',ParticipateOnGamifiedCoursView.as_view(),), 

    path('gamifiedcoursanswer/',MyAnswerCours.as_view(),), 
         
         
]