from django.shortcuts import render

# Create your views here.
def loginView(request):
    if request.user.is_authenticated:
        return redirect("/sessions")
    return render(request, 'profiles/login.html', {})