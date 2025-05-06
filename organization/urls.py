from django.urls import path

from .views import (
    TeamListView,
    TeamDetailView,
    TeamCreateView,
    TeamUpdateView,
    TeamDeleteView,
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    TaskCreateProjectView,
    ProjectDeleteView,
    TeamAddProjectView,
)


app_name = "organization"

urlpatterns = [
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("projects/<int:pk>/detail/", ProjectDetailView.as_view(), name="project-detail"),
    path("projects/create/", ProjectCreateView.as_view(), name="project-create"),
    path("projects/<int:pk>/add-task/", TaskCreateProjectView.as_view(), name="task-create-for-project"),
    path("projects/<int:pk>/add-team/", TeamAddProjectView.as_view(), name="project-add-team"),
    path("projects/<int:pk>/delete/", ProjectDeleteView.as_view(), name="project-delete"),
    path("teams/", TeamListView.as_view(), name="team-list"),
    path("teams/<int:pk>/detail/", TeamDetailView.as_view(), name="team-detail"),
    path("teams/create/", TeamCreateView.as_view(), name="team-create"),
    path("teams/<int:pk>/update/", TeamUpdateView.as_view(), name="team-update"),
    path("teams/<int:pk>/delete/", TeamDeleteView.as_view(), name="team-delete"),
]
