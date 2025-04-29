from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Task
from .forms import TaskSearchForm


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "operation/task_list.html"
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
    template_name = "operation/task_detail.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = ("name", "description", "deadline", "priority", "task_type", "assignees")
    template_name = "operation/task_form.html"
    success_url = reverse_lazy("operation:task-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = ("name", "description", "deadline", "priority", "task_type", "assignees", "is_completed")
    template_name = "operation/task_update.html"
    success_url = reverse_lazy("operation:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("operation:task-list")
