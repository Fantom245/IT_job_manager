from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
