from django.shortcuts import render, redirect
from profiles.models import Profile
from django.contrib.auth.models import User
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def loginView(request):
    if request.user.is_authenticated:
        return redirect("/sessions")
    return render(request, 'profiles/login.html', {})


class profileView(generic.ListView):
    template_name='profiles/profile.html'
    context_object_name = 'profile_list'
    #session_list = Session.objects.all()
                                    #objects.filter(date__gte=timezone.now())

    def get_queryset(self):
        return Profile.objects.all().last()

def updateProfile(request):
    if request.method == "POST":
        profile = Profile.objects.create(username = request.POST['Username'], about = request.POST['Bio'], year = request.POST['Year'])

        return HttpResponseRedirect(reverse('profilepage'))
    else:
        return render(request, 'profiles/profile.html', {'error': 'method is not post'} )


class updateProfileView(generic.ListView):
    template_name = 'profiles/updateProfile.html'
    context_object_name = 'profile_list'

    profile_list = Profile.objects.all()

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Profile.objects.all()
