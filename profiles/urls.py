from django.contrib import admin
from django.urls import path, include
from . import views

#3/20 ONLY one goes to loginView
urlpatterns = [
    path('', views.loginView, name="loginView"),
    path('logout', views.logoutView, name="logoutView"),
    path('profile/', views.profile, name='users-profile'),
    path('addCourse', views.addCourse, name="addCourse")
]