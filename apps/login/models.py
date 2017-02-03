from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import bcrypt

class UserManager(models.Manager):
	def register(self, request):
		is_valid = True
		if len(request.POST['name']) < 3:
			messages.error(request, "Name is required (must be at least 3 characters)")
			is_valid = False

		# if len(request.POST['last_name']) < 2:
		# 	messages.error(request, "Last Name is required")
		# 	is_valid = False

		if len(request.POST['username']) < 3:
			messages.error(request, "Username is required (must be at least 3 characters)")
			is_valid = False

		username_match = User.objects.filter(username=request.POST['username'])

		if len(username_match) != 0:
			messages.error(request, "Username is taken")
			is_valid = False

		if len(request.POST['password']) < 8:
			messages.error(request, "Password must be at least 8 character")
			is_valid = False

		if request.POST['password'] != request.POST['confirm_password']:
			messages.error(request, "password isn't identical")
			is_valid = False

		if not is_valid:
			return False

		hashed = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())

		new_user = User(
			name = request.POST['name'],
			# last_name = request.POST['last_name'],
			username = request.POST['username'],
			password = hashed,	
		)
		new_user.save()

		request.session['current_user'] = new_user.id
		request.session['current_user_name'] = new_user.name


		return True

	def login(self, request):
		user_logged = User.objects.filter(username=request.POST['username'])
		if len(user_logged) == 0:
			messages.error(request, 'This Username is not registered')
			return False

		user = user_logged[0]

		hashed_password = bcrypt.hashpw(request.POST['password'].encode('utf-8'), user.password.encode('utf-8'))
		if hashed_password != user.password:
			messages.error(request, 'Wrong Password')
			return False

		request.session['current_user'] = user.id
		request.session['current_user_name'] = user.name


		return True


class User(models.Model):
	name = models.CharField(max_length=30)
	# last_name = models.CharField(max_length=30)
	username = models.EmailField(max_length=30)
	password = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

