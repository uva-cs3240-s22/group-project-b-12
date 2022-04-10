#from curses import termname
#from msilib.schema import Class
from django.db import models

from django.contrib.auth.models import User

from django.contrib.postgres.fields import ArrayField 

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    id = models.BigIntegerField(primary_key = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    #classes = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user')

    def __str__(self):
        return self.user.username

class Test(models.Model):
    test = models.TextField()
# Create your models here.
# ["subject","catalog_number","class_section","class_number","class_title","class_topic_formal_desc","instructor","enrollment_capacity","meeting_days","meeting_time_start","meeting_time_end","term","term_desc"
class Courses(models.Model):
    subject= models.CharField(max_length=50, blank = True, null = True)
    catelog_number = models.CharField(max_length=10, blank = True, null = True)
    class_section = models.CharField(max_length=4000, blank = True, null = True)
    class_number = models.CharField(max_length=20, blank = True, null = True)
    class_title = models.SlugField(default = 'test')
    class_topic_formal_desc = models.CharField( max_length=50, blank = True, null = True)
    instructor = models.CharField(max_length=50, blank = True, null = True)
    enrollment_capacity = models.CharField(max_length=50, blank = True, null = True)
    meeting_days = models.CharField(max_length=50, blank = True, null = True)
    meeting_time_start = models.CharField(max_length=50, blank = True, null = True)
    meeting_time_end = models.CharField(max_length=50, blank = True, null = True)
    term = models.CharField(max_length=50, blank = True, null = True)
    term_desc = models.CharField(max_length=50, blank = True, null = True)

    def __str__(self):
        return self.name
