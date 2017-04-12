# Sara Lichtenstein, Senior Project 2017, Brain Food

from django import forms
from django.forms import ModelForm, modelformset_factory
from .models import User, Survey
from django.utils.safestring import mark_safe

#making nice things
class HorizRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

#registration
class RegisterForm(forms.Form):
	#first name
	firstName = forms.CharField(
		label = 'First Name',
		min_length = 1,
		max_length = 100,
		required = True
	)

	#last name
	lastName = forms.CharField(
		label = 'Last Name',
		min_length = 1,
		max_length = 100,
		required = True
	)

	#username, work on uniqueness
	user_name = forms.CharField(
		label = 'Username',
		min_length = 8,
		max_length = 50,
		required = True
	)

	#email
	email = forms.CharField(
		label = 'Email',
		min_length = 8,
		max_length = 100,
		required = True,

	)

	#password
	password = forms.CharField(
		label = 'Password',
		min_length = 8,
		widget = forms.PasswordInput(),
		required = True
	)

	#password check
	passwordCheck = forms.CharField(
		label = 'Password Check',
		min_length = 8,
		widget = forms.PasswordInput(), 
		required = True
	)

#login
class LoginForm(forms.Form):
	#username
	user_name = forms.CharField(
		label = 'Username',
		min_length = 8,
		max_length = 100,
		required = True
	)

	#password
	password = forms.CharField(
		label = 'Password',
		min_length = 8,
		widget = forms.PasswordInput(),
		required = True
	)

#initial survey
class SurveyForm(forms.Form):
	#mental activity
	MENT_ACT = (
		('N', 'None None None Non'),
		('L', 'Light Light Light Lig'),
		('M', 'Moderate Moderate Moderate Mo'),
		('R', 'Rigorous')
	)

	#projected mental activity
	mentalActivity = forms.ChoiceField(
		choices = MENT_ACT,
		label = 'Projected Mental Activity',
		required = True,
		widget = forms.RadioSelect(renderer=HorizRadioRenderer)
	)

	#PANAS
	PANAS = (
		(1, 'Very Slightly or Not At All So Much None None'),
		(2, 'A Little Bitty Bi'),
		(3, 'Moderately So Ho Ho'),
		(4, 'Quite A Bitty Bit BitB'),
		(5, 'Extremely')
	)

	interestedResponse = forms.ChoiceField(choices = PANAS, label = 'Interested', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	distressedResponse = forms.ChoiceField(choices = PANAS, label = 'Distressed', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	excitedResponse = forms.ChoiceField(choices = PANAS, label = 'Excited', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	upsetResponse = forms.ChoiceField(choices = PANAS, label = 'Upset', required = True,  widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	strongResponse = forms.ChoiceField(choices = PANAS, label = 'Strong', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	guiltyResponse = forms.ChoiceField(choices = PANAS, label = 'Guilty', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	scaredResponse = forms.ChoiceField(choices = PANAS, label = 'Scared', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	hostileResponse = forms.ChoiceField(choices = PANAS, label = 'Hostile', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	enthusiasticResponse = forms.ChoiceField(choices = PANAS, label = 'Enthusiastic', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	proudResponse = forms.ChoiceField(choices = PANAS, label = 'Proud', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	irritableResponse = forms.ChoiceField(choices = PANAS, label = 'Irritable', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	alertResponse = forms.ChoiceField(choices = PANAS, label = 'Alert', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	ashamedResponse = forms.ChoiceField(choices = PANAS, label = 'Ashamed', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	inspiredResponse = forms.ChoiceField(choices = PANAS, label = 'Inspired', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	nervousResponse = forms.ChoiceField(choices = PANAS, label = 'Nervous', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	determinedResponse = forms.ChoiceField(choices = PANAS, label = 'Determined', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	attentiveResponse = forms.ChoiceField(choices = PANAS, label = 'Attentive', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	jitteryResponse = forms.ChoiceField(choices = PANAS, label = 'Jittery', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	activeResponse = forms.ChoiceField(choices = PANAS, label = 'Active', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))

	afraidResponse = forms.ChoiceField(choices = PANAS, label = 'Afraid', required = True, widget = forms.RadioSelect(renderer=HorizRadioRenderer))