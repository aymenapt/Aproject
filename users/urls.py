from django.urls import path
from .views import CustomUserCreate ,LoginView

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(),),
    path('login/', LoginView.as_view(), name='login'),
    
    
]