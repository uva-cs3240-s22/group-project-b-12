from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    #Creates username for user
    #username = models.CharField(max_length = 100)

    #User can input some information about themselves
    about = models.TextField(max_length = 250)

    #User can indicate what year they are in
    year = models.IntegerField(default = 1)

    def __str__(self):
        return "My name is " + str(self.user) +" and I am a " + str(self.year)+" year. Here are a few details about me: "+ self.about +"."
