from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import TeamMemberListView, TeamMemberCreateView, TeamMemberEditView, TeamMemberDeleteView

# Add URL routing.

urlpatterns = [
    path('', TeamMemberListView.as_view(), name='team_member_list'),
    path('add/', TeamMemberCreateView.as_view(), name='team_member_add'),
    path('<int:pk>/edit/', TeamMemberEditView.as_view(), name='team_member_edit'),
    path('<int:pk>/delete/', TeamMemberDeleteView.as_view(), name='team_member_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])