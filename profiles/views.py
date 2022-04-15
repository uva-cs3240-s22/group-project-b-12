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
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=prof)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect("/")

    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profiles/profile.html', {'profile_form': profile_form}) 

def viewProfile(request, user_id):
    useri = get_object_or_404(User, pk=user_id)
    return render(request, 'profiles/viewProfile.html', {'userInfo': useri})

def sendMessage(request, user_id):
    useri = get_object_or_404(User, pk=user_id)
    #print(User.objects.get(pk=request.POST[user_id]).email, False)
    # emailRecepient = User.objects.get(pk=request.POST[user_id])
    return render(request, 'profiles/sendMsg.html', {'emailRecepient': useri.email})

def sendMessageGeneral(request):
    return render(request, 'profiles/sendMsg.html', {'emailRecepient': ''})
        
