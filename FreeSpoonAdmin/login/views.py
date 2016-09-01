from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
#from django.contrib.auth import authenticate, login, logout
from django.contrib import auth

from .forms import LoginForm, RegisterForm
from .models import User

# Create your views here.

def index(request):
	return HttpResponse("Hey, dear. You're at the login index.")

def signin(request):
	#import pdb
	#pdb.set_trace()
	if request.method == 'POST':
		loginform = LoginForm(request.POST)
		if loginform.is_valid():
			#username = request.POST.get('username')
			#password = request.POST.get('password')
			username = loginform.cleaned_data['username']
			password = loginform.cleaned_data['password']
			user = User.objects.filter(name__exact = username)
  			if user:
				#request.session['username'] = username
				user = User.objects.get(name=username)
				if user.password == password:
					return HttpResponseRedirect('http://192.168.102.9:8000/admin/')
				else:
					return render_to_response('login/signin_fail2.html')
			else:
				return render_to_response('login/signin_fail.html')
		else:
			return render(request, 'login/signin.html', {'form':loginform})
	else:
		loginform = LoginForm()

	return render(request, 'login/signin.html', {'form':loginform})

def signup(request):
	#import pdb
	#pdb.set_trace()
	if request.method == 'POST':
		registerform = RegisterForm(request.POST)
		if registerform.is_valid():
			username = registerform.cleaned_data['username']
			password = registerform.cleaned_data['password']
			password2 = registerform.cleaned_data['password2']
			email = registerform.cleaned_data['email']
			mob = registerform.cleaned_data['mob']
			if User.objects.filter(name__exact=username):
				return render_to_response('login/signup_fail.html')
			else:
				user = User.objects.create(
					name = username,
					password = password,
					email = email,
					tel = mob
				)
				if password == password2:
					request.session['name'] = username
					return render_to_response('login/signup_suc.html')
				else:
					return render_to_response('login/signup_fail2.html')
		else:
			return render(request, 'login/signup.html', {'form':registerform})
	else:
		registerform = RegisterForm()

	return render(request, 'login/signup.html', {'form':registerform})


