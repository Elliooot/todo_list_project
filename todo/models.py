from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200) # mission title
    completed = models.BooleanField(default=False) # mission status(whether finished or not)
    created_at = models.DateTimeField(auto_now_add=True) # mission creation time

    def __str__(self):
        return self.title