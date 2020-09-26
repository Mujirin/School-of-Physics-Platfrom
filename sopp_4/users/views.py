from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			# Flash message
			messages.success(request, f'Account created for {username}')
			# return redirect('blog-home')
			return render(request, 'users/register.html', {'form': form})
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form': form})