from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from studybud.models import Session
from django.utils import timezone
from django.views import generic
from django.urls import reverse

def sessions(request):
    return render(request, 'studybud/sessions.html', {})

def postSession(request):
    if request.method == "POST":
        session = Session.objects.create(date = timezone.now(), location = request.POST['location'], details = request.POST['details'], course = request.POST['course'])

        return HttpResponseRedirect(reverse('sessions'))
    else:
        return render(request, 'polls/sessions.html', {'error': 'method is not post'} )

class SessionPostView(generic.ListView):
    template_name = 'studybud/sessionSubmit.html'
    context_object_name = 'session_list'

    session_list = Session.objects.all()

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Session.objects.all()
