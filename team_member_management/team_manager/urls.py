""" URL configuration for team_member_management project. """

from django.contrib import admin
from django.urls import path, include

# Add app routing.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
]