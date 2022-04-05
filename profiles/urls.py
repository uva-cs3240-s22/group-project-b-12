from django.contrib import admin
from django.urls import path, include
from . import views
from .views import RegisterView

#3/20 ONLY one goes to loginView
urlpatterns = [
    path('', views.loginView, name="loginView"),
    path('register/', RegisterView.as_view(), name ='user-register'),
    path('logout', views.logoutView, name="logoutView"),
    path('profile/', views.profile, name="users-profile"),
]