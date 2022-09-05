from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
