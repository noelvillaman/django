from django.shortcuts import render

from .forms import ContactForm
from django.core.mail import send_mail, EmailMessage, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
	subject = ""
	message =""
	from_email = ""

	if request.method == "POST":
		form = ContactForm()
		if form.is_valid():
			subject = request.POST.get('subject', '')
			message = request.POST.get('message', '')
			from_email = request.POST.get('your_email', '')
			send_mail(subject, message, from_email, ['noel@namalliv.com'])
	else:
		# In reality we'd use a form class
		# to get proper validation errors.
		#return HttpResponse('Make sure all fields are entered and valid.')
		form = ContactForm()
		return render(request, 'contact/index.html', {'form': form})

def contact(request):
	return render(request, 'contact/contact_form.html')

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('your_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['noel@namalliv.com'])
            #email = EmailMessage(subject, message, from_email, to=['noel@namalliv.com'])
            #email.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')

def thanks(request):
	return render(request, 'home/salute.html')
	
