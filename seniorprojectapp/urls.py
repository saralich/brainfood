# Sara Lichtenstein, Senior Project 2017, Brain Food

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^index', views.index, name = 'index'),
	url(r'^register_form', views.register_form, name = 'register_form'),
	url(r'^login_form', views.login_form, name = 'login_form'),
	url(r'^survey_form', views.survey_form, name = 'survey_form'),
	url(r'^about', views.about, name = 'about'),
	url(r'^device_form', views.device_form, name = 'device_form'),
	#url(r'^user_form', views.user_form, name = 'user_form'),
	url(r'^.*/$', views.index, name = 'index'),
]