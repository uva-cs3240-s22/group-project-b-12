from django.shortcuts import render, redirect

# Create your views here.
def loginView(request):
    if request.user.is_authenticated:
        return redirect("/sessions")
    return render(request, 'profiles/login.html', {})

def profileView(request):
    return render(request, 'profiles/profile.html', {})
