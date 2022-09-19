from tabnanny import verbose
from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=200)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.task

    class Meta:
        verbose_name_plural = "Todo"