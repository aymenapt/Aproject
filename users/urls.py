from django.urls import path
from .views import CustomUserCreate ,LoginView, Verifyotp, UserUpdateView,  UserDelete, getallusers

app_name = 'users'
urlpatterns = [
    path('create/', CustomUserCreate.as_view(),),
    path('login/', LoginView.as_view(), name='login'),
    path('verifyotp/', Verifyotp.as_view(), name='verifyotp'),
    path('leadrboard/', getallusers.as_view()),
    path('users/<int:id>/', UserUpdateView.as_view(), name='user-update'),  
    path('users/delete/<int:id>/', UserDelete.as_view(), name='user-delete'),    

]