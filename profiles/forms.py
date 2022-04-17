from django import forms

from django.contrib.auth.models import User
from .models import Profile

class UpdateProfileForm(forms.ModelForm):
    user = forms.CharField(widget = forms.HiddenInput(), required = False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    
    class Meta:
        model = Profile
        fields = ['user', 'bio']