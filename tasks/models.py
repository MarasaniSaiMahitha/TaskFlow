from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField()

    priority = models.CharField(max_length=20, default="Medium")
    due_date = models.DateField(null=True, blank=True)

    status = models.CharField(max_length=50, default="Pending")