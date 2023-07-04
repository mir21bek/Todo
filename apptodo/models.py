from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    class Status(models.TextChoices):
        TODO = "TODO", "To do"
        IN_PROGRESS = "IN PROGRESS", "IN PROGRESS"
        DONE = "DONE", "DONE"

    status = models.CharField(
        max_length=100,
        choices=Status.choices,
        default=Status.TODO,
    )

    class Priority(models.TextChoices):
        HIGH = "HIGH", "HIGH"
        MIDL = "MIDL", "MIDL"
        LOW = "LOW", "LOW"

    priority = models.CharField(
        max_length=50,
        choices=Priority.choices,
        default=Priority.LOW,
    )

    title = models.CharField(max_length=150)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
