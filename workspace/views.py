from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task, Worker, Project, Team
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
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context["search_form"] = TaskSearchForm()

        name = self.request.GET.get("name", "")

        context["search_form"] = TaskSearchForm(initial={"name": name})
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
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        context["search_form"] = WorkerSearchForm()
        username = self.request.GET.get("username", "")

        context["search_form"] = WorkerSearchForm(initial={"username": username})
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


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Project
    template_name = "workspace/team_list.html"
    context_object_name = "team_list"
    queryset = Team.objects.all()
    paginate_by = 3


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team
    template_name = "workspace/team_detail.html"


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    fields = "__all__"
    template_name = "workspace/team_form.html"
    success_url = reverse_lazy("workspace:team-list")


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    template_name = "workspace/project_list.html"
    context_object_name = "project_list"
    queryset = Project.objects.all()
    paginate_by = 3


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    template_name = "workspace/project_detail.html"


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    fields = "__all__"
    template_name = "workspace/project_form.html"
    success_url = reverse_lazy("workspace:project-list")
