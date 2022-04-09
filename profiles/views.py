from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http.response import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def loginView(request):
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, 'profiles/login.html', {})

def logoutView(request):
    logout(request)
    return redirect("/")
