from django.contrib import admin
from django.urls import path, include
from . import views
#3/20 ONLY one goes to loginView
urlpatterns = [
    path('', views.loginView, name="loginView"),
    path('profilepage', views.profileView.as_view(), name="profileView"),
    path('profileupdate', views.updateProfile, name="update"),
    path('profileview', views.updateProfileView.as_view(), name="viewUpdate")
]
