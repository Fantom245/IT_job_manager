from django.urls import path
from .views import index, TaskListView
from .models import Task


app_name = "workspace"

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
]