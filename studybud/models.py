from django.db import models
from django.utils import timezone
import datetime
from profiles.models import Course
from django.contrib.auth.models import User

class Session(models.Model):
    #Maybe separate day and time as different fields at another point to more easily filter the session objects
    date = models.DateTimeField('meeting date')
    location = models.CharField(max_length=250)
    #Max length for UVA course format ('APMA 2130')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    #Description of the purpose of the session
    details = models.TextField(max_length = 250)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(User, related_name="users_attending") # Related_name field necessary to prevent reverse clash. Source: https://stackoverflow.com/questions/26955319/django-reverse-accessor-clashes
    #Want to use this function in ListView somehow.
    #   No need to see past studySessions (also no need to see filled sessions)
    #   Another alternative to this is using .filter in View return statement:
    #   "objects.filter(date__gte=timezone.now(), attendees__lt=8)"
    #   tried this but couldn't get .filter to work properly
    def is_in_future(self):
        now = timezone.now()
        return now<=self.date

    def __str__(self):
        return "Study session with "+str(self.attendees)+"attendees at "+ self.location+ " on "+str(self.date)+" for "+ str(self.course)+". Here are any additional details: " +self.details+ "."

class Spot(models.Model):
    location= models.CharField(max_length=250)