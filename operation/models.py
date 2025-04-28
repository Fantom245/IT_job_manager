from django.db import models

from people.models import Worker


# Model for selection
class Priority(models.TextChoices):
    URGENT = "1_Urgent", "Highest priority"
    HIGH = "2_High", "High priority"
    NORMAL = "3_Normal", "Normal priority"


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=9, choices=Priority.choices, default=Priority.NORMAL)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker)

    class Meta:
        ordering = ["priority",]

    def __str__(self):
        return self.name