from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from studybud.models import Session
from django.utils import timezone
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect

class sessionListView(LoginRequiredMixin,generic.ListView):
    login_url = '/profiles/'
    redirect_field_name = 'redirect_to'
    template_name='studybud/sessions.html'
    context_object_name = 'session_list'
    #session_list = Session.objects.all()
                                    #objects.filter(date__gte=timezone.now())
    def get_queryset(self):
        return Session.objects.all()

def postSession(request):
    if request.method == "POST":
        session = Session.objects.create(date = timezone.now(), location = request.POST['location'], details = request.POST['details'], course = request.POST['course'], host = User.objects.get(email=request.POST['Host']))
        session.attendees.add(User.objects.get(email=request.POST['Host']))
        return HttpResponseRedirect(reverse('sessions'))
    else:
        return render(request, 'polls/sessions.html', {'error': 'method is not post'} )

class SessionPostView(generic.ListView):
    login_url = '/profiles/'
    redirect_field_name = 'redirect_to'
    template_name = 'studybud/sessionSubmit.html, {var: 1}'
    context_object_name = 'session_list'

    session_list = Session.objects.all()

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Session.objects.all()


class SessionDetailView(generic.DetailView):
    login_url = '/profiles/'
    redirect_field_name = 'redirect_to'
    model = Session
    template_name= 'studybud/sessionDetail.html'

    def get_queryset(self):
        return Session.objects.all()

# class indexView(generic.DetailView):
#     template_name = 'studybud/index.html'

def index(request):
    return render(request, 'studybud/index.html')

def SessionSignUp(request):
    if request.method == "POST":
        session = Session.objects.get(id=request.POST['sessionid'])
        session.attendees.add(request.user)
        print("works")
    # session = request.POST['signUp']
    if request.method != "POST":
        print("hello")
    #print(session.id)
    return redirect("/")
