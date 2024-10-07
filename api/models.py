# api/models.py

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class UserGroup(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='groups')

    def __str__(self):
        return self.name
