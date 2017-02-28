from django.shortcuts import render

from .models import Person, Blog
from datetime import datetime
from django import forms


def index(request):
	try:
		person_list = Person.objects.all()
	except Person.DoesNotExist:
		raise Http404("Person does not exist")	
	return render(request, 'people/person_details.html', {'person_list': person_list})

def details(request, pID = '0'):
	try:
		p = Person.objects.get(id=pID)
	except Person.DoesNotExist:
		raise Http404("Person does not exist")
	return render(request, 'people/information.html', {'p':p})

def person_form(request, pID='0'):
	PersonForm = forms.form_for_instance(Person)
	f = PersonForm()
	message = 'Unknonw Request'

	p = Person.objects.get(id=pID)

	if request.method == 'GET':
		PersonForm = forms.form_for_instance(p)
		f = PersonForm
		message = 'Editing person %s ' % p.name

	if request.method == 'POST':
		if request.POST['submit'] == 'update':
			message = 'Update Request for %s ' % p.name
			PersonForm = forms.form_for_instance(p)
			if f.is_valid():
				message += ' Valid.'
			else:
				message += ' Invalid.'
	
	return render(request, 'People/person_form.html', {'pForm': f, 'message': message})

def add_blog_form(request, pID='0'):
	BlogForm = forms.form_for_model(Blog, fields=('title', 'text'))
	bf = BlogForm()
	message = 'Unknown Request'
	p = Person.objects.get(id=pID)

	if request.method == 'GET':
		message = 'Add Blog for %s ' % p.name

	if request.method == 'POST':
		if request.POST['submit'] == 'Add':
			bf = BlogForm(request.POST.copy())
			SaveForm = forms.form_for_model(Blog)
			postDict =  request.POST.copy()
			postDict['date'] = datetime.now()
			save_bf = SaveForm(postDict)
			if save_bf.is_valid():
				try:
					bObj = save_bf.save()
					p.blogs.add(bObj)
					p.save()
					message = 'Blog added to %s.' % p.name
				except:
					message = 'Database Error.'
			else:
				message = 'Invalid data in Form.'
	return render(request, 'People/add_blog_form.html', {'bForm': bForm, 'message': message})

	
