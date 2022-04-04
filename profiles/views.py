from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def loginView(request):
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, 'profiles/login.html', {})
    