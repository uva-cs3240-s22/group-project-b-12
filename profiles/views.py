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
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=prof)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')

    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profiles/profile.html', {'profile_form': profile_form}) 