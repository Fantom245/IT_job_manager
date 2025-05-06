from django.db import models
from people.models import Worker

from operation.models import Task


class Team(models.Model):
    name = models.CharField(max_length=255)
    workers = models.ManyToManyField(Worker)
    author = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name="authored_team")

    class Meta:
        ordering = ["name",]
        indexes = [
            models.Index(fields=["name",])
        ]

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    teams = models.ManyToManyField(Team)
    author = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name="authored_project")

    class Meta:
        ordering = ["name",]
        indexes = [
            models.Index(fields=["name",])
        ]

    def __str__(self):
        return f"Project {self.name}"
