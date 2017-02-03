from django.shortcuts import render, redirect
from ..login.models import User
from .models import Trip

# Create your views here.
def logout(request):
	request.session['current_user'] = 0
	request.session['current_user_name'] = 0

	return redirect('/')

def index(request):

	user = User.objects.get(id=request.session['current_user'])

	user_list = Trip.objects.filter(users=user)

	others_list = Trip.objects.exclude(users=user)

	context = {
		"user": user,
		"user_list": user_list,
		"others_list": others_list,
	}

	return render(request, 'belt/index.html', context)

def add(request):

	return render(request, 'belt/add.html')

def save(request):
	new = Trip.objects.new(request)

	if new:
		user = User.objects.get(id=request.session['current_user'])

		new_trip = Trip.objects.create(
			creator=user,
			destination=request.POST['destination'],
			description=request.POST['description'],
			start=request.POST['start'],
			end=request.POST['end'],

		)
		new_trip.users.add(user)
		new_trip.save()


		return redirect('/dashboard')

	return redirect('dashboard/add')

def info(request, id):
	trip = Trip.objects.get(id=id)
	travelers = trip.users.all()

	context = {
		"trip": trip,
		"travelers" : travelers
	}
	return render(request, 'belt/info.html', context)

def join(request):
	user = User.objects.get(id=request.session['current_user'])
	item = Trip.objects.get(id=request.POST['trip.id'])

	user.trips_list.add(item)
	user.save()

	return redirect('/dashboard')