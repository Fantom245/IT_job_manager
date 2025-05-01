from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import ProjectSearchForm, TeamSearchForm
from .models import Project, Team


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Project
    template_name = "organization/team_list.html"
    context_object_name = "team_list"
    queryset = Team.objects.all()
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TeamListView, self).get_context_data(**kwargs)
        context["search_form"] = TeamSearchForm()

        name = self.request.GET.get("name", "")

        context["search_form"] = TeamSearchForm(initial={"name": name})

        return context
    
    def get_queryset(self):
        form = TeamSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team
    template_name = "organization/team_detail.html"


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    fields = ("name", "workers",)
    template_name = "organization/team_form.html"
    success_url = reverse_lazy("organization:team-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class TeamUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Team
    fields = ("name", "workers",)
    template_name = "organization/team_update.html"
    success_url = reverse_lazy("organization:team-list")
    

class TeamDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Team
    success_url = reverse_lazy("organization:team-list")


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    template_name = "organization/project_list.html"
    context_object_name = "project_list"
    queryset = Project.objects.all()
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context["search_form"] = ProjectSearchForm()

        name = self.request.GET.get("name", "")

        context["search_form"] = ProjectSearchForm(initial={"name": name})

        return context
    
    def get_queryset(self):
        form = ProjectSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    template_name = "organization/project_detail.html"


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    fields = ("name", "description", "teams", "tasks",)
    template_name = "organization/project_form.html"
    success_url = reverse_lazy("organization:project-list")


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    fields = ("name", "description", "teams", "tasks",)
    template_name = "organization/project_update.html"
    success_url = reverse_lazy("organization:project-list")


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy("organization:project-list")
