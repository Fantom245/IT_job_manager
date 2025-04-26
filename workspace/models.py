from django.db import models
from django.contrib.auth.models import AbstractUser


# Model for selection
class Priority(models.TextChoices):
    URGENT = "Urgent", "Highest priority — requires immediate attention"
    HIGH = "High", "High priority — should be addressed soon after urgent tasks"
    NORMAL = "Normal", "Normal priority — standard tasks with no immediate urgency"


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=7, choices=Priority.choices, default=Priority.NORMAL)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField("Worker")

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Team(models.Model):
    name = models.CharField(max_length=255)
    workers = models.ManyToManyField(Worker)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    teams = models.ManyToManyField(Team)
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return f"Project {self.name}"
