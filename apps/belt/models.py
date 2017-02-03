from __future__ import unicode_literals

from django.db import models
from ..login.models import User
from django.contrib import messages
from datetime import datetime
from datetime import date

# Create your models here.

class Validation(models.Manager):
	def new(self, request):
		is_valid = True
		if len(request.POST['destination']) == 0:
			messages.error(request, "destination is required")
			is_valid = False

		if len(request.POST['description']) == 0:
			messages.error(request, "description is required")
			is_valid = False
		

		if not is_valid:
			return False

		return True

class Trip(models.Model):

	destination = models.CharField(max_length=20)
	description = models.TextField()
	start = models.DateField()
	end = models.DateField()

	users = models.ManyToManyField(User, related_name="trips_list")
	creator = models.ForeignKey(User)

	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	objects = Validation()