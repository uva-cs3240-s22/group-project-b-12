from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from studybud.models import Session
from studybud.models import Spot
from django.utils import timezone
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from profiles.models import Course
from django.contrib.auth.models import User
from django.shortcuts import redirect

class sessionListView(LoginRequiredMixin,generic.ListView):
    login_url = '/profiles/'
    redirect_field_name = 'redirect_to'
    template_name='studybud/sessions.html'
    context_object_name = 'session_list'
    #session_list = Session.objects.all()
                                    #objects.filter(date__gte=timezone.now())
    def get_queryset(self, **kwargs):
        user = self.request.user
        
        try:
            filter = self.request.GET.get('course', 'all')
            courses = user.profile.courses.all()

            if (filter=='all'):
                sessions = Session.objects.filter(course__in = courses) 
            else: 
                sessions = Session.objects.filter(course=filter)

            return sessions
        except:
            return []
            
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        user = self.request.user
        try:
            courses = user.profile.courses.all()
            context['courses'] = courses
        except:
            context['courses'] = []
        return context
    

def postSession(request):
    if request.method == "POST":
        courseID = request.POST["course"]
        coursei = Course.objects.get(id=courseID)
        session = Session.objects.create(date = timezone.now(), location = request.POST['location'], details = request.POST['details'], course=coursei, host = User.objects.get(email=request.POST['Host']))
        session.attendees.add(User.objects.get(email=request.POST['Host']))

        return HttpResponseRedirect(reverse('sessions'))
    else:
        return render(request, 'polls/sessions.html', {'error': 'method is not post'} )

class SessionPostView(generic.ListView):
    login_url = '/profiles/'
    redirect_field_name = 'redirect_to'
    template_name = 'studybud/sessionSubmit.html'
    context_object_name = 'session_list'
    session_list = Session.objects.all()
 
     
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        user = self.request.user
        courses = user.profile.courses.all()
        print(courses)
        print("!!!")
        context['courses'] = courses
        return context
        return context

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

    
class profileView(generic.ListView):
    template_name='studybud/studySpots.html'
    context_object_name = 'spot_list'
    #session_list = Session.objects.all()
                                    #objects.filter(date__gte=timezone.now())
    spot_list = Spot.objects.all()
    def get_queryset(self):
        return Spot.objects.all()
