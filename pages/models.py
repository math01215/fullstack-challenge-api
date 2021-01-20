from django.db import models
from users.models import User

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.title