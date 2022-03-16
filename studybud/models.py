from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class StudySession(models.Model):
    # Location, Number of attendees (which will have the option to be anonymous),
    #   Date/ Time, Course for which the work will be on, Extra optional detail text (maybe what specific assignment)
    date_time = models.DateTimeField('Date and time of session')
    attendees = models.IntegerField(default = 1) #1 for creator
    location = models.CharField(max_length = 100) #Could specify Building, floor, Room number/ area
    #Will this be its own model
    course = models.CharField(max_length = 9)
    def __str__(self):
        return "Study Session for "+self.course+" at " +self.location+" at "+str(self.date_time)+". There are currently "+str(self.attendees)+" students signed up."
