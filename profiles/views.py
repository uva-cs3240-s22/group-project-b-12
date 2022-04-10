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
from .models import Profile, Courses
import requests

# Create your views here.
def loginView(request):
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, 'profiles/login.html', {})

def logoutView(request):
    logout(request)
    return redirect("/")

@login_required
def profile(request):
    prof, created = Profile.objects.get_or_create(user=request.user)
    messages.success(request, request.user)
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=prof)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')

    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profiles/profile.html', {'profile_form': profile_form}) 
def get_classes(request):
    if 'name' in request.GET:
        name = request.GET['name']
        url =  'https://www.themealdb.com/api/json/v1/1/search.php?subject=%s' % name
        all_classes = {}
        response = requests.get(url)
        data = response.json()
        courses = data['records']
        for i in courses:
            courses_data = Courses( 
                 subject= i[0],
                 catelog_number = i[1],
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
            courses_data.save()
            all_classes = Courses.objects.all().order_by('-id')
    return render(request, 'profiles/profile.html', {"all_classes" : all_classes})

            
