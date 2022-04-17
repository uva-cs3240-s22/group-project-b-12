from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from studybud.models import Session
from django.utils import timezone
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from profiles.models import Course


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
        session = Session.objects.create(date = timezone.now(), location = request.POST['location'], details = request.POST['details'], course=coursei)
      
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