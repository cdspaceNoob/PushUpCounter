from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    count = models.IntegerField()
    time = models.CharField(max_length=255)

    def __str__(self):
        return "user: "+self.username+" count: "+self.count+" time: "+self.time

    class Meta:
        ordering = ['date_joined']
