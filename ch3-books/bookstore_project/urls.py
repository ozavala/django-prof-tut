from django.contrib import admin
from django.urls import path, include  # new

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/login/', include('allauth.urls')),

    # Local apps
    path('', include('pages.urls')),

]
