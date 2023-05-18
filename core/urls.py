from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # Oauth
    # Project URLs
    path('admin/', admin.site.urls),
    # User Management
    path('', include('users.urls')),
    path('',include('challenges.urls'))
   
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)