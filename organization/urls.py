from django.urls import path
from .views import (
    TeamListView,
    TeamDetailView,
    TeamCreateView,
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
)


app_name = "organization"

urlpatterns = [
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("projects/<int:pk>/detail/", ProjectDetailView.as_view(), name="project-detail"),
    path("projects/create/", ProjectCreateView.as_view(), name="project-create"),
    path("teams/", TeamListView.as_view(), name="team-list"),
    path("teams/<int:pk>/detail/", TeamDetailView.as_view(), name="team-detail"),
    path("teams/create/", TeamCreateView.as_view(), name="team-create"),
]
