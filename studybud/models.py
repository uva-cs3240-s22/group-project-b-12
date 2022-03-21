from django.db import models
from django.utils import timezone
import datetime

class Session(models.Model):
    attendees = models.IntegerField(default = 1)
    #Maybe separate day and time as different fields at another point to more easily filter the session objects
    date = models.DateTimeField('meeting date')
    location = models.CharField(max_length=250)
    #Max length for UVA course format ('APMA 2130')
    course = models.CharField(max_length = 9)
    #Description of the purpose of the session
    details = models.TextField(max_length = 250)

    def __str__(self):
        return "Study session with "+str(self.attendees)+" at "+ self.location+ " on "+str(self.date)+" for "+self.course+". Here are any additional details: " +self.details+ "."