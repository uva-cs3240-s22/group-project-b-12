"""studybud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profiles/', include('profiles.urls')),
    path('', views.sessionListView.as_view(), name='sessions'),
    #functional URL
    path('sessions/post/', views.postSession, name='postSession'),
    #Input URL
    path('sessions/submit/', views.SessionPostView.as_view(), name='submitSession'),
    #Clicking on the Session object takes you to it's specific detail view
    path('sessions/<int:pk>/', views.SessionDetailView.as_view(), name='sessionDetail'),
    path('session/signup/',views.SessionSignUp, name="signUp")
] 
