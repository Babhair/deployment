from django.shortcuts import render, redirect
from .models import User
# Create your views here.

def index(request):

	return render(request, 'login/index.html')

def register(request):
	did_register = User.objects.register(request)
	
	if did_register:
		return render(request, 'login/success.html')
	else:
		return redirect('/')

def login(request):

	did_login = User.objects.login(request)

	if did_login:
		return render(request, 'login/success.html')
	else:
		return redirect('/')	