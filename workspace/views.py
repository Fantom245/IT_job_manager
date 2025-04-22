from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic

from .models import Task, Worker


# @login_required
def index(request):
    tasks = Task.objects.all()
    workers = Worker.objects.all()

    context = {
        "tasks": tasks,
        "workers": workers,
    }

    return render(request, "workspace/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task
    template_name = "workspace/task_list.html"
    context_object_name = "task_list"


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "workspace/task_detail.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "workspace/task_form.html"
    success_url = reverse_lazy("workspace:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("workspace:task-list")
