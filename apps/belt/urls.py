from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'logout$', views.logout),
	url(r'add$', views.add),
	url(r'save$', views.save),
	url(r'trip/(?P<id>\d+)$', views.info),
	url(r'join$', views.join),



]