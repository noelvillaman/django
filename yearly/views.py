from django.shortcuts import render
import calendar
from datetime import date, datetime
import mlbgame
import math

def month_days(d, n):
	hold_days = []
	for j in range(d):
		hold_days.append("  ") 
	i = 1
	while i <= n:
		if i < 10:
			# hold_days.append("")
			hold_days.append(i)
		else:
			hold_days.append(i)
		# if (i+d) % 7 == 0:
		# 	hold_days.append(' ')
		i = i + 1
	return hold_days

def calendarListView(request):

	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	days = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ]
	"""
		This variables is to get the name of the month
	"""

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

	one_month = list_of_days_in_months

	return render(request, 'yearly/calendar.html', {'one_month': one_month, 'months': months, 'days': days })

def monthid(num):
	monthid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
	if num in monthid:
		return num
	else:
		return 0

def calendarMonthView(request, month_id=0):
	month = calendar.Calendar(firstweekday=0)
	weekDays = month.iterweekdays()
	monthDay = month.itermonthdates(2017, 1)
	monthid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

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

	for j in range(days_d[month_id]):
		month_2017.append(" ") 
	i = 1
	while i <= days_month_n[month_id]:
		if i < 10:
			month_2017.append(i)
		else:
			month_2017.append(i)
		i = i + 1

	shores = []
	for i in range(1, 32):
		shores.append(str(i) + " Jugar con Ezra e Ishah")
	return render(request, 'yearly/month.html', {'shores': shores, 'month_2017': month_2017, 'weekDays': weekDays, })

def day_calendarMonthView(request, num):
	days = []
	for i in num:
		days.append(i)
	return render(request, 'yearly/day_month.html', {'num' : num, 'days': days })

def calendarListView_month(request, month_game=1):

	locations = {
		"Angels": "Angel Stadium",
		"Tigers": "Comerica Park " ,
		"Red Sox": "Fenway Park " ,
		"Rangers": "Globe Life Park",
		"White Sox": "Guaranteed Rate Field" ,
		"Royals":"Kauffman Stadium " ,
		"Astros":"Minute Maid Park " ,
		"Athletics":"Oakland Alameda Coliseum " ,
		"Orioles":"Oriole Park at Camden Yards " ,
		"Indians": "Progressive Field ",
		"Blue Jays": "Rogers Centre ",
		"Mariners": "Safeco Field ",
		"Twins": "Target Field ",
		"Rays": "Tropicana Field " ,
		"Yankees": "Yankee Stadium " ,
		"Giants": "AT&T Park ",
		"Cardinals": "Busch Stadium " ,
		"D-backs": "Chase Field " ,
		"Mets": "Citi Field " ,
		"Phillies": "Citizens Bank Park ",
		"Rockies": "Coors Field ",
		"Dodgers": "Dodger Stadium ",
		"Reds": "Great American Ball Park " ,
		"Marlins": "Marlins Park ",
		"Brewers":"Miller Park " ,
		"Nationals": "Nationals Park " ,
		"Padres": "Petco Park " ,
		"Pirates": "PNC Park ",
		"Braves": "Turner Field ",
		"Cubs": "Wrigley Field "
	}

	months = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
	days = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ]
	"""
		This variables is to get the name of the month
	"""
	
	month_title = "January"
	for k, v in months.items():
		if int(month_game) == k:
			month_title = v
	""""""

	the_game_day = 0
	int(month_game)
	if int(month_game) > 0 and int(month_game) <= 12:
		the_game_day = int(month_game)
	else:
		the_game_day = 1

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

	a_month_games = mlbgame.games(2017, the_game_day, home="Angels", away="Angels")

	mlbgames = mlbgame.combine_games(a_month_games)

	one_month = month_days(days_d[the_game_day-1], days_month_n[the_game_day-1])

	# one_month = zip(list_of_days_in_months, mlbgames)
	game_days = []
	name_months = []
	name_days = []
	hr = []


	for game in mlbgames:
		game_days.append(game.date.date().day)
		name_months.append(game.date.date().strftime("%B"))
		name_days.append(game.date.date().strftime("%A"))
		hr.append(game.date.time())

	return render(request, 'yearly/calendar_month.html', {'one_month': one_month, 'months': months, 'days': days, 
		'mlbgames' : mlbgames,'game_days': game_days, 'locations': locations, 'the_game_day': the_game_day, 'month_title': month_title })

def game_view(request, month, day, year, game_id):

	months = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
	days = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ]
	"""
		This variables is to get the name of the month
	"""
	
	month_title = "January"
	for k, v in months.items():
		if int(month) == k:
			month_title = v
	""""""
	""" add ordinal ending to the day number """
	ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
	day = ordinal(int(day))

	game_one = "This game will have it results soon. Tune again for that"
	return render(request, 'yearly/game_view.html', {'game_one': game_one, 'month':month_title, 'day':day, 'year': year })