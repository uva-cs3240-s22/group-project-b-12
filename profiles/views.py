from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm, ContactForm, ContactFormFilled
from django.contrib import messages
from .models import Profile, Courses, Course, Contact
import requests
from django.utils.datastructures import MultiValueDictKeyError
from .models import Profile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
import sendgrid
import os
from sendgrid.helpers.mail import *
# For django env variables. Source: https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f
import environ

env = environ.Env()
environ.Env.read_env()

# Create your views here.
def loginView(request):
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, 'profiles/login.html', {})

def logoutView(request):
    logout(request)
    return redirect("/")

# Source: https://dev.to/earthcomfy/django-user-profile-3hik
def profile(request):
    if not request.user.is_authenticated:
        return redirect("/")
    prof, created = Profile.objects.get_or_create(user=request.user)
    coursesEnrolledIn = request.user.profile.courses.all()
    if request.method == 'POST':
    #     name = request.POST.get('coursesid')
    #     print(name, "!!!")
        # print(name)
        # if name == 'toSave':
        #     print('enters here')
        #     classAdd = user.objects.get(id=request.POST['']).Profile
        #     classAdd.classes.add(request.courses)
        #     return render(request, 'profiles/profile.html')
    # else: 
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=prof)
        if profile_form.is_valid():
            profile_form.save()
            saved_message = "Your changes have been saved"
            messages.success(request, saved_message)
            return redirect(to='profiles:users-profile')
    elif request.method == 'GET':
        profile_form = UpdateProfileForm(instance=request.user.profile)
        url =  'https://api.devhub.virginia.edu/v1/courses/'
        response = requests.get(url)
        print(response)
        data = response.json()
    # print(data['class_schedules']['records'])
        try:
            name = request.GET.get('name')
        except MultiValueDictKeyError:
            name = False

        print(name)
        if name is not None and name != '': 
            try: 
                name = name.split()
                subj = name[0].upper()
                num = name[1]
                courses = data['class_schedules']['records']
                course_display = set()
                for i in courses: 
                    if i[0] == subj and i[1] == num and (i[0],i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8],i[9], i[10],i[11], i[12]) not in course_display:
                    #put this in a conditional 
                        courses_data = Courses(
                            subject= i[0],
                            catalog_number = i[1],
                            class_section = i[2],
                            class_number = i[3],
                            class_title = i[4],
                            class_topic_formal_desc = i[5],
                            instructor = i[6],
                            enrollment_capacity = i[7],
                            meeting_days = i[8],
                            meeting_time_start = timeConvert(i[9]),
                            meeting_time_end = timeConvert(i[10]),
                            term = i[11],
                            term_desc = i[12]  
                        )
                        #subject, catalog number, class number, class title, instructor 
                        course_display.add((i[0],i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8],i[9], i[10],i[11], i[12]))
                        courses_data.save()
                        #print(course_display)

            except: 
                num = 0
                error_message = str(name[0]) + ' not in valid format. Please format input as SUBJECT CATALOGNUMBER (ex: CS 3240)'
                messages.warning(request, error_message)

            all_classes = Courses.objects.filter(subject =  subj , catalog_number = num).values('subject','catalog_number','class_section','class_number', 'class_title', 'instructor', 'term_desc', 'meeting_time_start', 'meeting_time_end').distinct()
            return render(request, 'profiles/profile.html', {'profile_form': profile_form, 'all_classes': all_classes, 'coursesEnrolledIn': coursesEnrolledIn}) 
        else: 
            return render(request, 'profiles/profile.html', {'profile_form': profile_form, 'coursesEnrolledIn': coursesEnrolledIn})
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)
        
        return render(request, 'profiles/profile.html', {'profile_form': profile_form, 'coursesEnrolledIn': coursesEnrolledIn})

def timeConvert(ds):
    hours, minutes, seconds = ds.split(":")
    hours, minutes, seconds = int(hours), int(minutes), int(seconds)
    #print(hours)
    #print(minutes)
    #print(seconds)
    setting = "AM"
    if hours > 12:
        setting = "PM"
        hours = hours - 12
    #print(hours)
    #print(minutes)
    #print(("%02d:%02d" + setting) % (hours, minutes))
    return (("%02d:%02d" + setting) % (hours, minutes)) 
def addCourse(request):
    if request.method == 'POST':
        courseInstructor = request.POST['courseInstructor']
        courseSubject = request.POST['courseSubject']
        courseCatNum = request.POST['courseCatNum']
        user = request.user

        #If course object doesn't already exist, create it
        if len(Course.objects.filter(instructor=courseInstructor, subject=courseSubject, catalog_number=courseCatNum)) == 0:
             user.profile.courses.create(instructor=courseInstructor, catalog_number = courseCatNum, subject = courseSubject)
        #Else, add course object to user's courses
        else:
            course = Course.objects.get(instructor=courseInstructor, catalog_number = courseCatNum, subject = courseSubject)
            user.profile.courses.add(course)  
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # To redirect to previous site. Source: https://stackoverflow.com/questions/12758786/redirect-return-to-same-previous-page-in-django

def viewProfile(request, user_id):
    if not request.user.is_authenticated:
        return redirect("/")
    useri = get_object_or_404(User, pk=user_id)
    return render(request, 'profiles/viewProfile.html', {'userInfo': useri})

# To send email with user parameter
def sendMessage(request, user_id):
    if not request.user.is_authenticated:
        return redirect("/")
    useri = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = ContactFormFilled(request.POST)
        if form.is_valid():
            form.save()
            try:
                SENDGRID_API_KEY = env('SENDGRID_API_KEY')
            except:
                pass

            sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
            user = request.user
            email_subject = f'Studybud: New Message from {user.first_name} {user.last_name}: {form.cleaned_data["subject"]}' #TODO: Make useri the sender
            email_message = form.cleaned_data['message']
            from_email = "b12studybud@gmail.com"
            to_email = useri.email
            print(SENDGRID_API_KEY)
            mail = Mail(from_email, to_email, email_subject, email_message)
            sg.client.mail.send.post(request_body=mail.get())
            return render(request, 'profiles/emailSent.html')

    form = ContactFormFilled()
    form.Meta.email = useri.email
    context = {'emailRecepient': useri.email,'form': form}
    return render(request, 'profiles/sendMsg.html', context)
  
def removeCourse(request):
    user = request.user
    if request.method == "POST":
        course = Course.objects.get(id=request.POST['courseid'])
        user.profile.courses.remove(course)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # To redirect to previous site. Source: https://stackoverflow.com/questions/12758786/redirect-return-to-same-previous-page-in-django
