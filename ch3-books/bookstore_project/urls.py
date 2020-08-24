from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
   # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/login/', include('django.contrib.auth.urls')),

     # Local apps
    path('accounts/', include('users.urls')),
    path('', include('pages.urls')),
    
]
