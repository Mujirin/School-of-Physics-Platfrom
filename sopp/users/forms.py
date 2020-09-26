from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField() # By default required = True

	class Meta:
		model = User
		fields = ['username', 'password1', 'password2', 'email']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField() # Default required = True

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']