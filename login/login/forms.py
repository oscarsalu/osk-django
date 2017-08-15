from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext, ugettext_lazy as _

class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(
		label=_("Email"),
		widget=forms.EmailInput,
		required = True)
	
	firstname = forms.CharField(
		label=_("First Name"),
		widget=forms.TextInput,
		required = True)
	
	class Meta:
		model = User
		fields = ('firstname','username', 'email', 'password1', 'password2')

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['firstname']

		if commit:
			user.save()

		return user