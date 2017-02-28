from django import forms

class ContactForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your complete name'}))
	your_email = forms.CharField(label='Your email', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': '123hotmail@domain.com'}))
	subject = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Message Subject'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message here.'}), required=True)
	cc_myself = forms.BooleanField(required=False)
