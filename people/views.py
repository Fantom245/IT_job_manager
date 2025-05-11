from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Worker
from .forms import WorkerSearchForm

from operation.models import Task
from organization.models import Project, Team


def index(request):
    tasks = Task.objects.all()
    workers = Worker.objects.all()
    number_tasks = Task.objects.all().count()
    number_workers = Worker.objects.all().count()
    number_projects = Project.objects.all().count()
    number_teams = Team.objects.all().count()

    context = {
        "tasks": tasks,
        "workers": workers,
        "number_projects": number_projects,
        "number_teams": number_teams,
        "number_workers": number_workers,
        "number_tasks": number_tasks,
    }

    return render(request, "people/index.html", context=context)


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    template_name = "people/worker_list.html"
    context_object_name = "worker_list"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        context["search_form"] = WorkerSearchForm()
        username = self.request.GET.get("username", "")

        context["search_form"] = WorkerSearchForm(initial={"username": username})
        return context
    
    def get_queryset(self):
        queryset = Worker.objects.all()
        form = WorkerSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class WorkerCreateView(generic.CreateView):
    model = Worker
    fields = ("username", "password", "first_name", "last_name", "email", "position")
    template_name = "people/worker_form.html"
    success_url = reverse_lazy("people:worker-list")

    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data["password"])
        return super().form_valid(form)


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "people/worker_detail.html"


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("people:worker-list")
