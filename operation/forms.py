from django import forms
from django.db.models import Q

from .models import Task
from people.models import Worker


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by task name"}
        )
    )


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "deadline", "priority", "task_type", "assignees"]

    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project', None)
        # Важно — передать оставшиеся kwargs (включая 'instance') в super().__init__
        super().__init__(*args, **kwargs)

        if project:
            self.fields['assignees'].queryset = Worker.objects.filter(
                team__in=project.teams.all()
            ).distinct()
