from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Project, Team


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Project
    template_name = "organization/team_list.html"
    context_object_name = "team_list"
    queryset = Team.objects.all()
    paginate_by = 3


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team
    template_name = "organization/team_detail.html"


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    fields = "__all__"
    template_name = "organization/team_form.html"
    success_url = reverse_lazy("organization:team-list")


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    template_name = "organization/project_list.html"
    context_object_name = "project_list"
    queryset = Project.objects.all()
    paginate_by = 3


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    template_name = "organization/project_detail.html"


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    fields = "__all__"
    template_name = "organization/project_form.html"
    success_url = reverse_lazy("organization:project-list")


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("organization:project-list")


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy("organization:project-list")
