from django.urls import path
from .views import CreateChallenges, CreateImages, CreateParagrahe, CreateTitels, CreateTasks

app_name = 'users'

urlpatterns = [
    path('createchalenges/', CreateChallenges.as_view(),),
    path('creatTaskImages/', CreateImages.as_view(),),
    path('creatTaskParagrahe/', CreateParagrahe.as_view(),),
    path('creatTaskTitels/', CreateTitels.as_view(),),
    path('creatTask/', CreateTasks.as_view(),),
    
    
    
]