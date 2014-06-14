from match.models import UserProfile, MatchRequest
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('callback_url',)

class MatchRequestForm(forms.ModelForm):
	class Meta:
		model = MatchRequest
