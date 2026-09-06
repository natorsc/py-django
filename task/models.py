from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "pk"]

    def __str__(self):
        return f"{self.title}"
