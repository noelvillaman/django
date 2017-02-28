from django.db import models
from django.contrib.auth.models import User


gender_list = (('M', 'Male'), ('F', 'Female'))

class Blog(models.Model):
	title = models.CharField('Title', max_length=200)
	date = models.DateField('Date', blank=True, null=True)
	text = models.TextField('Text', max_length=2048)

class Person(models.Model):
	firstname = models.CharField('name', max_length=100)
	lastname = models.CharField('lastname', max_length=100)
	birthday = models.DateField('Birthday', blank=True, null=True)
	gender = models.CharField(max_length=1, choices=gender_list, null=True)
	email = models.EmailField('Email', blank=True)
	favoriteURL = models.URLField('myURL', blank=True, null=True)
	text = models.TextField('Desc', max_length=500, blank=True)
	blogs = models.ManyToManyField(Blog, blank=True)
	
	def __str__(self):
		return '%s %s' % (self.firstname, self.lastname)
		
	class Admin:
		pass
