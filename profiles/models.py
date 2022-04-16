from django.db import models

from django.contrib.auth.models import User


# Extending User Model Using a One-To-One Link
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     bio = models.TextField()
#     classes = models.ManyToManyField(Courses)
#     def __str__(self):
#         return self.user.username

class Test(models.Model):
    test = models.TextField()
# Create your models here.
class Courses(models.Model):
    subject= models.CharField(max_length=50, blank = True, null = True)
    catalog_number = models.CharField(max_length=10, blank = True, null = True)
    class_section = models.CharField(max_length=4000, blank = True, null = True)
    class_number = models.CharField(max_length=20, blank = True, null = True)
    class_title = models.CharField(max_length=20, blank = True, null = True)
    class_topic_formal_desc = models.CharField( max_length=50, blank = True, null = True)
    instructor = models.CharField(max_length=50, blank = True, null = True)
    enrollment_capacity = models.CharField(max_length=50, blank = True, null = True)
    meeting_days = models.CharField(max_length=50, blank = True, null = True)
    meeting_time_start = models.CharField(max_length=50, blank = True, null = True)
    meeting_time_end = models.CharField(max_length=50, blank = True, null = True)
    term = models.CharField(max_length=50, blank = True, null = True)
    term_desc = models.CharField(max_length=50, blank = True, null = True)

class Course(models.Model):
    instructor = models.CharField(max_length=50, blank = True, null = True)
    catalog_number = models.CharField(max_length=10, blank = True, null = True)
    subject= models.CharField(max_length=50, blank = True, null = True)

#many to many field django 
    def __str__(self):
        return self.subject + self.catalog_number
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField()
    classes = models.ManyToManyField(Courses)
    courses = models.ManyToManyField(Course)
    def __str__(self):
        return self.user.username