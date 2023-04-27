from django.urls import path
from .views import CreateChallenges

app_name = 'users'

urlpatterns = [
    path('createchalenges/', CreateChallenges.as_view(),),
    
    
    
]