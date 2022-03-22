from django.http import HttpResponse
from django.shortcuts import render
from studybud.models import Session
from django.utils import timezone


def sessions(request):
    return render(request, 'studybud/sessions.html', {})

def postSession(request):
    if request.method == "POST":
        session = Session.objects.create(date = timezone.now(), location = request.POST['location'], details = request.POST['details'], course = request.POST['course'])

        return HttpResponseRedirect(reverse('studybud:sessions'))
    else:
        return render(request, 'polls/sessions.html', {'error': 'method is not post'} )

