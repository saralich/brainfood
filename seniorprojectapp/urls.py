# Sara Lichtenstein, Senior Project 2017, Brain Food

from django.conf.urls import *
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^index', views.index, name = 'index'),
	url(r'^register_form', views.register_form, name = 'register_form'),
	url(r'^login_form', views.login_form, name = 'login_form'),
	url(r'^survey_form', views.survey_form, name = 'survey_form'),
	url(r'^about', views.about, name = 'about'),
	url(r'^trial_form', views.trial_form, name = 'trial_form'),
	#url(r'^user_form', views.user_form, name = 'user_form'),
	url(r'^.*/$', views.index, name = 'index'),
]