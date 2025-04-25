from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task, Worker
from .forms import TaskSearchForm, WorkerSearchForm


@login_required
def index(request):
    tasks = Task.objects.all()
    workers = Worker.objects.all()

    context = {
        "tasks": tasks,
        "workers": workers,
    }

    return render(request, "workspace/index.html", context=context)


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "workspace/task_list.html"
    context_object_name = "task_list"
    queryset = Task.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context["search_form"] = TaskSearchForm()
        return context
    
    def get_queryset(self):
        form = TaskSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "workspace/task_detail.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "workspace/task_form.html"
    success_url = reverse_lazy("workspace:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("workspace:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("workspace:task-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    template_name = "workspace/worker_list.html"
    context_object_name = "worker_list"
    queryset = Worker.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        context["search_form"] = WorkerSearchForm()
        return context
    
    def get_queryset(self):
        form = WorkerSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    fields = ("username", "password", "first_name", "last_name", "email", "position")
    template_name = "workspace/worker_form.html"
    success_url = reverse_lazy("workspace:worker-list")

    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data["password"])
        return super().form_valid(form)


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "workspace/worker_detail.html"


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("workspace:worker-list")
