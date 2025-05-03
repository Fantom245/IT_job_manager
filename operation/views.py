from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from organization.models import Project

from .models import Task
from .forms import TaskSearchForm


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "operation/task_list.html"
    context_object_name = "task_list"
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context["search_form"] = TaskSearchForm()

        name = self.request.GET.get("name", "")

        context["search_form"] = TaskSearchForm(initial={"name": name})
        context["task_count"] = self.get_queryset().count()
        
        return context
    
    def get_queryset(self):
        queryset = Task.objects.all()
        form = TaskSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "operation/task_detail.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = ("name", "description", "deadline", "priority", "task_type", "assignees")
    template_name = "operation/task_form.html"
    success_url = reverse_lazy("operation:task-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class TaskCreateProjectView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = ("name", "description", "deadline", "priority", "task_type", "assignees")

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=self.kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.project = self.project
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("organization:project-detail", kwargs={"pk": self.project.pk})


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = ("name", "description", "deadline", "priority", "task_type", "assignees", "is_completed")
    template_name = "operation/task_update.html"
    success_url = reverse_lazy("operation:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("operation:task-list")
