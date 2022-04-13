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
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, ('Your sessions were successfully updated!'))
        else:
            messages.error(request, ('Unable to complete request'))
        return redirect("main:userpage")
        profile_form = UpdateProfileForm(instance=request.user.profile)
        session_id = request.POST.get("session_pk")
        session = Product.objects.get(id = session_id)
        request.user.profile.sessions.add(session)
        return redirect('/profiles/profile')
    return render(request, template_name="studybud/sessions.html")



	#return render(request = request, template_name ="main/user.html", context = {"user":request.user,
	#	"user_form": user_form, "profile_form": profile_form })
