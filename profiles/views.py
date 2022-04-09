from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .forms import RegisterForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
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
    return render(request, 'profiles/profile.html')
class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'profiles/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})
