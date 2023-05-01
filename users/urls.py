from django.urls import path
from .views import CustomUserCreate ,LoginView, Verifyotp

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(),),
    path('login/', LoginView.as_view(), name='login'),
    path('verifyotp/', Verifyotp.as_view(), name='verifyotp'),
    
    
]