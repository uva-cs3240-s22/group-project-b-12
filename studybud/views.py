from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from studybud.models import Session
from django.utils import timezone
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from profiles.models import Profile



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
        session = Session.objects.create(date = timezone.now(), location = request.POST['location'], details = request.POST['details'], course = request.POST['course'])

        return HttpResponseRedirect(reverse('sessions'))
    else:
        return render(request, 'polls/sessions.html', {'error': 'method is not post'} )

class SessionPostView(generic.ListView):
    login_url = '/profiles/'
    redirect_field_name = 'redirect_to'
    template_name = 'studybud/sessionSubmit.html'
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

def redirect_view(request):
    return redirect('/profiles/profile')

def sessions(request):
    if request.method == "POST":
        session_id = request.POST.get("session_pk")
        session = Product.objects.get(id = session_id)
        request.user.profile.products.add(session)
        #messages.success(request,(f'{session} added to sessions.'))
        return redirect('/profiles/profile')
    #sessions = Session.objects.all()
    return render(request, template_name="studybud/sessions.html")
