from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return "user: "+self.username

    class Meta:
        ordering = ['date_joined']


class Data(models.Model):
    count = models.IntegerField()
    time = models.CharField(max_length=255)
    created = models.DateTimeField()

    def __str__(self):
        return "count: "+self.count+" time: "+self.time

    class Meta:
        ordering = ['created']
