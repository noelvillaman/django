# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from datetime import datetime, date
from django import forms
import os
import codecs
import calendar
from django.conf import settings
from .forms import Nombre
from chartit import DataPool, Chart
from .models import MonthlyWeatherByCity, FedaralDays
import random
import datetime
import time
import mlbgame
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
	fedays = FedaralDays.objects.all()
	theDate = date.today()
	this_month = theDate.month
	today = theDate.day
	mydate = datetime.datetime.now()
	mymonth = mydate.strftime("%B")

	days_d = [
		calendar.MONDAY, calendar.THURSDAY, calendar.THURSDAY,
		calendar.SUNDAY,calendar.TUESDAY, calendar.FRIDAY,
		calendar.SUNDAY,calendar.WEDNESDAY, calendar.SATURDAY, 
		calendar.MONDAY, calendar.THURSDAY,calendar.SATURDAY,
	]
	
	days_month_n = [
		(date(2017, 2, 1) - date(2017, 1, 1)).days, (date(2017, 3, 1) - date(2017, 2, 1)).days, (date(2017, 4, 1) - date(2017, 3, 1)).days, 
		(date(2017, 5, 1) - date(2017, 4, 1)).days, (date(2017, 6, 1) - date(2017, 5, 1)).days, (date(2017, 7, 1) - date(2017, 6, 1)).days, 
		(date(2017, 8, 1) - date(2017, 7, 1)).days, (date(2017, 9, 1) - date(2017, 8, 1)).days, (date(2017, 10, 1) - date(2017, 9, 1)).days, 
		(date(2017, 11, 1) - date(2017, 10, 1)).days, (date(2017, 12, 1) - date(2017, 11, 1)).days, (date(2018, 1, 1) - date(2017, 12, 1)).days, 
	]

	month_2017 = []

	for j in range(days_d[this_month-1]):
		month_2017.append(" ") 
	i = 1
	while i <= days_month_n[this_month-1]:
		if i < 10:
			month_2017.append(i)
		else:
			month_2017.append(i)
		i = i + 1

	shores = []
	for i in range(1, 32):
		shores.append(str(i) + " Jugar con Ezra e Ishah")
	return render(request, 'home/index.html', {'shores': shores, 'month_2017': month_2017, 'fedays': fedays, 'today': today, 'mymonth': mymonth })

class EmailForm(forms.Form):
	title = forms.CharField(max_length=50)
	sender = forms.EmailField()
	date = forms.DateTimeField()
	text = forms.CharField(max_length=200)

def contact_view(request):
	eForm = EmailForm()
	return render_to_response('home/contact_form.html', {'eForm' : eForm })


def php_view(request):
	return render(request, 'home/home.php')

def reading_view(request):
	file = codecs.open(os.path.join(
		settings.PROJECT_ROOT, 'nmc321-final.txt'), 'r', 'utf-8')
	return render(request, 'home/reading.html', {'file': file})

myarr = [
	[ 8, 2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8],
	[49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0],
	[81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65],
	[52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91],
	[22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
	[24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50],
	[32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
	[67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21],
	[24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
	[21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95],
	[78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92],
	[16,39,5,42,96,35,31,47,55,58,88,24,00,17,54,24,36,29,85,57],
	[86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58],
	[19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40],
	[4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66],
	[88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69],
	[4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36],
	[20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16],
	[20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54],
	[1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48],
]

def bakedArray(request):
	d1=d2=d3=d4=group_of_results=[] 
	grande = 0
	cuatro = 0
	temp = 0
	for i in range(20):
		for j in range(20):
			try:
				#To the right direction
				grande =  myarr[i][j] *  myarr[i][j+1] *  myarr[i][j+2] *  myarr[i][j+3]
				group_of_results.append(grande)
				if grande == 70600674:
					cuatro = [myarr[i][j],  myarr[i][j+1], myarr[i][j+2],  myarr[i][j+3]]
				#To the right diagonal direction
				d2 = myarr[i][j] *  myarr[i+1][j+1] *  myarr[i+2][j+2] *  myarr[i+3][j+3]
				group_of_results.append(d2)
				if d2 == 70600674:
					cuatro = [myarr[i][j],  myarr[i+1][j+1], myarr[i+2][j+2],  myarr[i+3][j+3]]
				#To the down direction
				d3 = myarr[i][j] *  myarr[i+1][j] *  myarr[i+2][j] *  myarr[i+3][j]
				group_of_results.append(d3)
				if d3 == 70600674:
					cuatro = [myarr[i][j],  myarr[i+1][j+1], myarr[i][j+2],  myarr[i][j+3]]
				""" To the left direction is not needed because it was calculated on the right direction, prove me wrong in this."""
				# d5 = myarr[i][j] *  myarr[i][j-1] *  myarr[i][j-2] *  myarr[i][j-3]
				# group_of_results.append(d5)
				# if d5 == 70600674:
				# 	cuatro = [myarr[i][j],  myarr[i][j+1], myarr[i][j+2],  myarr[i][j+3]]
				#up left diagonal, not neeeded, it was calculated with the down right diagonal, prove me wrong.
				# d6 = myarr[i][j] *  myarr[i-1][j-1] *  myarr[i-2][j-2] *  myarr[i-3][j-3]
				# group_of_results.append(d6)
				# if d6 == 70600674:
				# 	cuatro = [myarr[i][j],  myarr[i-1][j-1], myarr[i-2][j-2],  myarr[i-3][j-3]]
				#Up not needed, it was calculated coming down, prove me wrong.
				# d7 = myarr[i][j] *  myarr[i-1][j] *  myarr[i-2][j] *  myarr[i-3][j]
				# group_of_results.append(d7)
				# if d7 == 70600674:
				# 	cuatro = [myarr[i][j],  myarr[i][j+1], myarr[i][j+2],  myarr[i][j+3]]
				d8 = myarr[i][j] *  myarr[i+1][j-1] *  myarr[i+2][j-2] *  myarr[i+3][j-3]
				group_of_results.append(d8)
				if d8 == 70600674:
					cuatro = [myarr[i][j],  myarr[i+1][j-1], myarr[i+2][j-2],  myarr[i+3][j-3]]
			except IndexError:
				continue
	#print cuatro
	grande = max(group_of_results)		
	return render(request, 'home/bigarray.html', {'grande': grande, 
		'group_of_results': group_of_results, 'cuatro': cuatro, 'myarr': myarr})

@csrf_exempt
def get_name(request):
	numbers = []
	if request.method == 'POST':
		nombre = request.POST.get('nombre')
		apellido = request.POST.get('apellido')
		table = request.POST.get('table1')

		for i in range(1, 13):
			numbers.append(i*int(table))

		context = {
			'nombre': nombre,
			'apellido': apellido,
			'numbers': numbers,
			'table': table
		}

		template = loader.get_template('home/result.html')

		return HttpResponse(template.render(context, request))
	else:
		template = loader.get_template('home/nombre.html')
		return HttpResponse(template.render())


def view_chart(request):
	xdata = ["Apple", "Appricto", "Avocado", "Banana", "Boyseenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
	ydata = [52, 48, 160, 94, 75, 490, 46, 17]

	extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
	charttype = {'x':xdata, 'y1': ydata, 'extra1': extra_serie}
	chartdata = "pieChart"

	data = {
		'charttype': charttype,
		'chartdata': chartdata,
	}

	return render_to_response('home/piechart.html', data)

def monthname(month_num):
	names ={1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
            7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
	return names[month_num]
	

def weather_view(request):
	#datapool with the data we want to retrieve
	weatherdata = DataPool(series=[{'options': {
		'source': MonthlyWeatherByCity.objects.all()},
		'terms': [
		'month',
		'boston_temp']}
		])

	#Create chart object
	cht = Chart(
		datasource=weatherdata,
		series_options =
		[{'options':{
		'type': 'pie',
		'stacking': False},
		'terms':{
		'month': [
		'boston_temp']
		}}],
		chart_options = 
          {'title': {
               'text': 'Monthly Temperature of Boston'}},
        x_sortf_mapf_mts = (None, monthname, False))
	#Send the chart object to the template
	return render_to_response('home/weather.html', {'weatherchart': cht})

def month_list(request):
	shores = []
	for i in range(1, 32):
		shores.append(str(i) + " Jugar con Ezra e Ishah")
	return render('home/index.html', {'shores': shores})


def calendarListView(request):

	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	days = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ]
	list_of_days_in_months = []
	

	days_d = [
		calendar.MONDAY, calendar.THURSDAY, calendar.THURSDAY,
		calendar.SUNDAY,calendar.TUESDAY, calendar.FRIDAY,
		calendar.SUNDAY,calendar.WEDNESDAY, calendar.SATURDAY, 
		calendar.MONDAY, calendar.THURSDAY,calendar.SATURDAY,
	]
	

	
	days_month_n = [
		(date(2017, 2, 1) - date(2017, 1, 1)).days, (date(2017, 3, 1) - date(2017, 2, 1)).days, (date(2017, 4, 1) - date(2017, 3, 1)).days, 
		(date(2017, 5, 1) - date(2017, 4, 1)).days, (date(2017, 6, 1) - date(2017, 5, 1)).days, (date(2017, 7, 1) - date(2017, 6, 1)).days, 
		(date(2017, 8, 1) - date(2017, 7, 1)).days, (date(2017, 9, 1) - date(2017, 8, 1)).days, (date(2017, 10, 1) - date(2017, 9, 1)).days, 
		(date(2017, 11, 1) - date(2017, 10, 1)).days, (date(2017, 12, 1) - date(2017, 11, 1)).days, (date(2018, 1, 1) - date(2017, 12, 1)).days, 
	]

	for i in range(len(days_d)):
		list_of_days_in_months.append(month_days(days_d[i], days_month_n[i]))

	return render(request, 'yearly/calendar.html', {'one_month': one_month, 'list': list_of_days_in_months[0], 'months': months, 'days': days, 
		'mlbgames' : mlbgames,'game_days': game_days, 'locations': locations })

def thanks(request):
	return render(request, 'home/salute.html')

def assignment4(request):
	return render(request, 'home/assignment4.html')
