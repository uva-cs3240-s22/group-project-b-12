from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm
from django.contrib import messages
from .models import Profile, Courses, Course
import requests
from django.utils.datastructures import MultiValueDictKeyError
from .models import Profile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse

# Create your views here.
def loginView(request):
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, 'profiles/login.html', {})

def logoutView(request):
    logout(request)
    return redirect("/")

# Source: https://dev.to/earthcomfy/django-user-profile-3hik
@login_required
def profile(request):
    prof, created = Profile.objects.get_or_create(user=request.user)
    messages.success(request, request.user)
    courses = request.user.profile.courses.all()
    print(courses)
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
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
            return render(request, 'profiles/profile.html', {'profile_form': profile_form})
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
            name = name.split()
            subj = name[0]
            num = name[1]
            courses = data['class_schedules']['records']
            course_display = set()
            for i in courses: 
                if i[0] == subj and i[1] == num and i[3] not in course_display:
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
                        meeting_time_start = i[9],
                        meeting_time_end =i[10],
                        term = i[11],
                        term_desc = i[12]  
                    
                    )
                    #subject, catalog number, class number, class title, instructor 
                    course_display.add(i[3])
                    courses_data.save()
            print(course_display)
            all_classes = Courses.objects.filter(subject =  subj , catalog_number = num).values('subject','catalog_number','class_section','class_number', 'class_title', 'instructor').distinct()
            return render(request, 'profiles/profile.html', {'profile_form': profile_form, 'all_classes': all_classes, 'courses': courses}) 
        else: 
            return render(request, 'profiles/profile.html', {'profile_form': profile_form, 'courses': courses})
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)
        
        return render(request, 'profiles/profile.html', {'profile_form': profile_form, 'courses': courses})

def addCourse(request):
    if request.method == 'POST':
        courseInstructor = request.POST['courseInstructor']
        courseSubject = request.POST['courseSubject']
        courseCatNum = request.POST['courseCatNum']
        user = request.user
        print(courseInstructor)
        print(courseSubject)
        print(courseCatNum)

        #If course object doesn't already exist, create it
        if len(Course.objects.filter(instructor=courseInstructor, subject=courseSubject, catalog_number=courseCatNum)) == 0:
             user.profile.courses.create(instructor=courseInstructor, catalog_number = courseCatNum, subject = courseSubject)
        #Else, add course object to user's courses
        else:
            course = Course.objects.get(instructor=courseInstructor, catalog_number = courseCatNum, subject = courseSubject)
            user.profile.courses.add(course)
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # To redirect to previous site. Source: https://stackoverflow.com/questions/12758786/redirect-return-to-same-previous-page-in-django

def viewProfile(request, user_id):
    useri = get_object_or_404(User, pk=user_id)
    return render(request, 'profiles/viewProfile.html', {'userInfo': useri})

def sendMessage(request, user_id):
    useri = get_object_or_404(User, pk=user_id)
    #print(User.objects.get(pk=request.POST[user_id]).email, False)
    # emailRecepient = User.objects.get(pk=request.POST[user_id])
    return render(request, 'profiles/sendMsg.html', {'emailRecepient': useri.email})

