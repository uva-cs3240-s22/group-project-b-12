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
from django.utils.datastructures import MultiValueDictKeyError



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
            for i in courses: 
                if i[0] == subj and i[1] == num:
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
                    courses_data.save()
            all_classes = Courses.objects.filter(subject =  subj , catalog_number = num).distinct('class_number')

            return render(request, 'profiles/profile.html', {'profile_form': profile_form, 'all_classes': all_classes}) 
        else: 
            return render(request, 'profiles/profile.html', {'profile_form': profile_form})
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)
        
        return render(request, 'profiles/profile.html', {'profile_form': profile_form})


#move entire thign into the profile view 

         #   courses_data = Courses( #make this singular 
      
         #   all_classes = Courses.objects.all().order_by('-id') #change to filter by move to outside the for loop 

