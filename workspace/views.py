from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
