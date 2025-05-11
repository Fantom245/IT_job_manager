from django.db import models
from django.contrib.auth.models import AbstractUser


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    class Meta:
        ordering = ["username",]
        indexes = [
            models.Index(fields=["username"])
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
