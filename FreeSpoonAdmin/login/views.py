from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import LoginForm
from .models import User

# Create your views here.

def index(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('http://192.168.102.9:8000/admin/')
	else:
		form = LoginForm()

	return render(request, 'login/index.html', {'form':form})


