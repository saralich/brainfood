# Sara Lichtenstein, Senior Project 2017, Brain Food

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import *
from django.views.generic import FormView
from django.core.urlresolvers import reverse
from django.db.models import Max
from django.core.mail import EmailMessage
from django.utils import dateformat
from django.contrib import auth
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse

import datetime
import time
import models

from .models import User, Survey
from .forms import RegisterForm, SurveyForm, LoginForm

def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

def about(request):
	template = loader.get_template('about.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

def trial_form(request):
	template = loader.get_template('trial_form.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

#1. Register Form
def register_form(request):
	#initialize user 
	firstName = lastName = user_name = password = user_email = ''
	
	#check for post
	if request.method == 'POST':
		
		#if valid, pull the info
		form = RegisterForm(request.POST)
		if form.is_valid():
			newFirstName = request.POST.get('firstName', '')
			newLastName = request.POST.get('lastName', '')
			newUser_name = request.POST.get('user_name', '')
			newPassword = request.POST.get('password', '')
			newUserEmail = request.POST.get('email', '')

			#check if things are already registered
			if User.objects.filter(user_name = newUser_name).exists():
				state = "This username already exists."
				return render(request, 'register_form.html', {'form':form, 'state':state})

			if User.objects.filter(user_email = newUserEmail).exists():
				state = "This email is already registered."
				return render(request, 'register_form.html', {'form':form, 'state':state})

			else:
				newUser = User(
					first_name = newFirstName,
					last_name = newLastName,
					user_name = newUser_name,
					password = newPassword,
					user_email = newUserEmail
				)
				newUser.save()
				user_id = newUser.user_id
				print("new user success reg")
				state = "User successfully created."
				return HttpResponseRedirect('/login_form/')
	else:
		print("not posted reg")
		form = RegisterForm()

	state = "Please enter new user information"
	return render(request, 'register_form.html', {'form':form, 'state':state})

#2. Survey Form
def survey_form(request):
	#initialize model variables
	mentalActivity = interestedResponse = distressedResponse = excitedResponse = ''
	upsetResponse = strongResponse = guiltyResponse = scaredResponse = hostileResponse = ''
	enthusiasticResponse = proudResponse = irritableResponse = alertResponse = ashamedResponse = ''
	inspiredResponse = nervousResponse = determinedResponse = attentiveResponse = ''
	jitteryResponse = activeResponse = afraidResponse = ''

	#check for post
	if request.method == 'POST':
	
	#if valid, pull the info
		form = SurveyForm(request.POST)
		if form.is_valid():

			newMentalActivity = request.POST.get('mentalActivity')
			newInterestedResponse = request.POST.get('interestedResponse')
			newDistressedResponse = request.POST.get('distressedResponse')
			newExcitedResponse = request.POST.get('excitedResponse')
			newUpsetResponse = request.POST.get('upsetResponse')
			newStrongResponse = request.POST.get('strongResponse')
			newGuiltyResponse = request.POST.get('guiltyResponse')
			newScaredResponse = request.POST.get('scaredResponse')
			newHostileResponse = request.POST.get('hostileResponse')
			newEnthusiasticResponse = request.POST.get('enthusiasticResponse')
			newProudResponse = request.POST.get('proudResponse')
			newIrritableResponse = request.POST.get('irritableResponse')
			newAlertResponse = request.POST.get('alertResponse')
			newAshamedResponse = request.POST.get('ashamedResponse')
			newInspiredResponse = request.POST.get('inspiredResponse')
			newNervousResponse = request.POST.get('nervousResponse')
			newDeterminedResponse = request.POST.get('determinedResponse')
			newAttentiveResponse = request.POST.get('attentiveResponse')
			newJitteryResponse = request.POST.get('jitteryResponse')
			newActiveResponse = request.POST.get('activeResponse')
			newAfraidResponse = request.POST.get('afraidResponse')
			
			#save new survey response
			newSurvey = Survey(
				mental_activity = newMentalActivity,
				interested = newInterestedResponse,
				distressed = newDistressedResponse,
				excited = newExcitedResponse,
				upset = newUpsetResponse,
				strong = newStrongResponse,
				guilty = newGuiltyResponse,
				scared = newScaredResponse,
				hostile = newHostileResponse,
				enthusiastic = newEnthusiasticResponse,
				proud = newProudResponse,
				irritable = newIrritableResponse,
				alert = newAlertResponse,
				ashamed = newAshamedResponse,
				inspired = newInspiredResponse,
				nervous = newNervousResponse,
				determined = newDeterminedResponse,
				attentive = newAttentiveResponse,
				jittery = newJitteryResponse,
				active = newActiveResponse,
				afraid = newAfraidResponse
			)
			newSurvey.save()
			#print that it worked
			print("Log: new survey saved")
			state = "New survey response recorded."
			#redirect to next page
			return HttpResponseRedirect('/trial_form/')

	else:
		form = SurveyForm()

	state = "Please enter accurate survey information"
	return render(request, 'survey_form.html', {'form':form, 'state':state})

#3. Login Form
@login_required
def login_form(request):
	#initialize model variables
	user_name = password = ''
	
	#check for post
	if request.method == 'POST':
	
	#if valid, pull info
		form = LoginForm(request.POST)
		if form.is_valid():
			user_name = request.POST.get('user_name')
			password = request.POST.get('password')
			user = User.objects.get(user_name = user_name)
			
			#checks
			if request.user.is_authenticated:
				if user.password == password:
					state = "Successful login."
					request.session['user_name'] = user.user_name
					print("auth works")
					return HttpResponseRedirect('/survey_form/')
				else:
					state = "Password did not match."
					print("password doesnt match")
					return render(request, 'login_form.html', {'form':form, 'state':state})

			else:
				state = "Invalid username."
				print("invalid username")
				return render(request, 'login_form.html', {'form':form, 'state':state})

	else:
		print("not posted")
		form = LoginForm()

	state = "Please enter valid username and password combination"
	return render(request, 'login_form.html', {'form':form, 'state':state})