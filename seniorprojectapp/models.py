from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator

# Sara Lichtenstein, Senior Project 2017, Brain Food

#create user class for login
class User(models.Model):
	#key field def
	user_id = models.AutoField(primary_key = True)
	def __unicode__(self):
		return self.user_id

	#generic username requirements
	user_name = models.CharField(
		"Username",
		max_length = 50, 
		blank = False
	)
	def __unicode__(self):
		return self.user_name
	
	#generic password requirements
	password = models.CharField(
		"Password",
		max_length = 20, 
		blank = False, 
		validators = [MinLengthValidator(8, "Your password must contain at least 8 characters.")]
	)
	def __unicode__(self):
		return self.password

	#first name
	first_name = models.CharField(
		"First Name",
		max_length = 50,
		validators = [RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters allowed')]
	)
	def __unicode__(self):
		return self.first_name

	#last name
	last_name = models.CharField(
		"Last Name",
		max_length = 50,
		validators = [RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters allowed')]
	)
	def __unicode__(self):
		return self.last_name

	#email
	email = models.CharField(
		"Email",
		max_length = 100
	)
	def __unicode__(self):
		return self.email

	pass

#create survey for better suggestions
class Survey(models.Model):
	survey_id = models.AutoField(primary_key=True, blank=False)
	def __unicode__(self):
		return self.survey_id

	#mental activity
	MENT_ACT = (
		('N', 'None'),
		('L', 'Light'),
		('M', 'Moderate'),
		('R', 'Rigorous')
	)

	#projected mental activity
	mental_activity = models.CharField(
		max_length = 1,
		choices = MENT_ACT,
		default = 'N'
	)
	def __unicode__(self):
		return self.mental_activity

	#PANAS
	PANAS = (
		('1', 'Very Slightly or Not At All'),
		('2', 'A Little'),
		('3', 'Moderately'),
		('4', 'Quite a Bit'),
		('5', 'Extremely')
	)

	interested = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3',
	)

	distressed = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	excited = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	upset = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	strong = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	guilty = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	scared = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	hostile = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	enthusiastic = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	proud = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	irritable = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	alert = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	ashamed = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	inspired = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	nervous = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	determined = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	attentive = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	jittery = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	active = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)

	afraid = models.CharField(
		max_length = 1,
		choices = PANAS,
		default = '3'
	)
