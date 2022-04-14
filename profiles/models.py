from django.db import models
from studybud.models import Session
from django.contrib.auth.models import User

# Source: https://dev.to/earthcomfy/django-user-profile-3hik
# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField()
    sessions = models.ManyToManyField(Session)

    def __str__(self):
        return self.user.username

class Test(models.Model):
    test = models.TextField()
# Create your models here.
