from django.urls import path
from .views import *

urlpatterns = [
    path('createchalenges/', CreateChallenges.as_view(),),
    path('creatTaskImages/', CreateImages.as_view(),),
    path('creatTaskParagrahe/', CreateParagrahe.as_view(),),
    path('creatTaskTitels/', CreateTitels.as_view(),),
    path('createfile/', CreateFile.as_view(),),
    path('createquestion/', CreateQuestion.as_view(),),
    path('createvideo/', CreateVideo.as_view(),),
    path('creatTask/', CreateTasks.as_view(),),
    path('updatetask/<int:id>/', TaskUpdateView.as_view()),
    path('creatrules/', CreateChallegeRules.as_view(),),
    path('videoUpdateDelete/<int:id>/', VideoUpdateView.as_view()),
    path('questionUpdateDelete/<int:id>/', QuestionUpdateView.as_view()),
    path('titelUpdateDelete/<int:id>/', TitelUpdateView.as_view()),
    path('imageUpdateDelete/<int:id>/', ImagesUpdateView.as_view()),
    path('paragraphUpdateDelete/<int:id>/', ParagrapheUpdateView.as_view()),
    path('fileUpdateDelete/<int:id>/', FileUpdateView.as_view()),
    path('planifychallenge/<int:challenge_id>/', PlanifyChallenge.as_view()),
    path('getPlanfiedchallenges/', GetPlanfiedchallenges.as_view()),
    path('getads/', GetSposorAds.as_view()),
    path('getNonPlanfiedchallenges/', GetNONPlanfiedchallenges.as_view()),
    path('registre/', RegeitreOnChallenge.as_view()),
    path('participate/', ParticipateOnChallenge.as_view()),
    path('answer/', MyAnswer.as_view()),



    path('filalparticipate/<int:id>/', FinalParticipate.as_view()),


    
    
    
]