from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Oauth
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    # Project URLs
    path('admin/', admin.site.urls),
    # User Management
    path('', include('users.urls')),
    path('',include('challenges.urls'))
   
    
] 