from django.urls import path

from .views import (
    index,
    WorkerListView,
    WorkerCreateView,
    WorkerDetailView,
    WorkerDeleteView,
)


app_name = "workspace"

urlpatterns = [
    path("", index, name="index"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
]
