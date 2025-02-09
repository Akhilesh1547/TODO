from django.db import models
from django.contrib.auth.models import User

class TODO(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicit ID field
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=[
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Study', 'Study')
    ], default='Personal')
    priority = models.CharField(max_length=10, choices=[
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    ], default='Medium')
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
