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
		max_length = 50, 
		blank = False
	)
	def __unicode__(self):
		return self.user_name
	
	#generic password requirements
	password = models.CharField(
		max_length = 20, 
		blank = False, 
		validators = [MinLengthValidator(8, "Your password must contain at least 8 characters.")]
	)
	def __unicode__(self):
		return self.password

	#first name
	first_name = models.CharField(
		max_length = 50,
		blank = False,
		validators = [RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters allowed')]
	)
	def __unicode__(self):
		return self.first_name

	#last name
	last_name = models.CharField(
		max_length = 50,
		blank = False,
		validators = [RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters allowed')]
	)
	def __unicode__(self):
		return self.last_name

	#email
	user_email = models.CharField(
		blank = False,
		max_length = 100
	)
	def __unicode__(self):
		return self.user_email

	pass

#create survey for better suggestions
class Survey(models.Model):
	survey_id = models.AutoField(primary_key=True)
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
		blank = False,
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
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.interested

	distressed = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.distressed

	excited = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.excited

	upset = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.upset

	strong = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.strong

	guilty = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.guilty

	scared = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.scared

	hostile = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.hostile

	enthusiastic = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.enthusiastic

	proud = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.proud

	irritable = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.irritable

	alert = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.alert

	ashamed = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.ashamed

	inspired = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.inspired

	nervous = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.nervous

	determined = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.determined

	attentive = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.attentive

	jittery = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.jittery

	active = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.active

	afraid = models.CharField(
		blank = False,
		max_length = 1,
		choices = PANAS
	)
	def __unicode__(self):
		return self.afraid

	pass
