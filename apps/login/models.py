from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import bcrypt

class UserManager(models.Manager):
	def register(self, request):
		is_valid = True
		if len(request.POST['first_name']) < 2:
			messages.error(request, "First Name is required")
			is_valid = False

		if len(request.POST['last_name']) < 2:
			messages.error(request, "Last Name is required")
			is_valid = False

		if len(request.POST['email']) == 0:
			messages.error(request, "Email is required")
			is_valid = False

		email_match = User.objects.filter(email=request.POST['email'])

		if len(email_match) != 0:
			messages.error(request, "Email has been used before")
			is_valid = False

		if request.POST['password'] != request.POST['confirm_password']:
			messages.error(request, "password isn't identical")
			is_valid = False

		if not is_valid:
			return False

		hashed = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())

		new_user = User(
			first_name = request.POST['first_name'],
			last_name = request.POST['last_name'],
			email = request.POST['email'],
			password = hashed,			
		)
		new_user.save()

		request.session['current_user'] = new_user.id
		request.session['current_user_name'] = new_user.first_name
		request.session['welcome_message'] = "registered"


		return True

	def login(self, request):
		emails_logged = User.objects.filter(email=request.POST['email'])
		if len(emails_logged) == 0:
			messages.error(request, 'This Email is not registered')
			return False

		user = emails_logged[0]

		hashed_password = bcrypt.hashpw(request.POST['password'].encode('utf-8'), user.password.encode('utf-8'))
		if hashed_password != user.password:
			messages.error(request, 'Wrong Password')
			return False

		request.session['current_user'] = user.id
		request.session['welcome_message'] = "logged in"
		print user.id


		return True


class User(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	password = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

