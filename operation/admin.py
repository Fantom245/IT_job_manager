from django.contrib import admin

from .models import Task, TaskType


admin.site.register(TaskType)
admin.site.register(Task)
