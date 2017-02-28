from django import forms

class SubmitPersonForm(forms.Form):
	personForm = forms.CharField(label='Summit Person')

class AddressForm(object):
	"""docstring for 
AddressForm"""
	name = forms.CharField()
	address = forms.CharField()
	email = forms.CharField()

		
