from django import forms

class Nombre(forms.Form):
	name = forms.CharField(label='Your name ', max_length=100)
	created_at = forms.DateTimeField()
