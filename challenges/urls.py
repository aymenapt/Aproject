from django.urls import path
from .views import *



urlpatterns = [
    path('createchalenges/', CreateChallenges.as_view(),),
    path('creatTaskImages/', CreateImages.as_view(),),
    path('creatTaskParagrahe/', CreateParagrahe.as_view(),),
    path('creatTaskTitels/', CreateTitels.as_view(),),
    path('creatTask/', CreateTasks.as_view(),),
    path('planifychallenge/<int:challenge_id>/', PlanifyChallenge.as_view()),
    path('getPlanfiedchallenges/', GetPlanfiedchallenges.as_view()),
    path('getNonPlanfiedchallenges/', GetNONPlanfiedchallenges.as_view()),
    
    
    
]