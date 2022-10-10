from tabnanny import verbose
from typing_extensions import Required
from django.db import models
from django.urls import reverse

class Todo(models.Model):
    task = models.CharField(max_length=200)
    added_date = models.DateField(auto_now_add=True)
    due_time = models.CharField(max_length=200)

    def __str__(self):
        return self.task
