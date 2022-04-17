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
from .models import Profile, Contact
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

# To send email with user parameter
def sendMessage(request, user_id):
    useri = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = ContactFormFilled(request.POST)
        if form.is_valid():
            form.save()
            SENDGRID_API_KEY = env('SENDGRID_API_KEY') 

            sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
            email_subject = f'Studybud: New Message from {useri.email}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            from_email = Email("jmj6ry@virginia.edu")
            to_email = useri.email
            mail = Mail(from_email, to_email, email_subject, email_message)
            sg.client.mail.send.post(request_body=mail.get())
            return render(request, 'profiles/emailSent.html')

    form = ContactFormFilled()
    form.Meta.email = useri.email
    context = {'emailRecepient': useri.email,'form': form}
    return render(request, 'profiles/sendMsg.html', context)

# To send email with no user parameter
def sendMessageGeneral(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            SENDGRID_API_KEY = env('SENDGRID_API_KEY') 

            sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
            email_subject = f'Studybud: New Message from {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            from_email = Email("jmj6ry@virginia.edu")
            to_email = [form.cleaned_data["email"]]
            mail = Mail(from_email, to_email, email_subject, email_message)
            sg.client.mail.send.post(request_body=mail.get())
            return render(request, 'profiles/emailSent.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'profiles/sendMsg.html', context)
        
