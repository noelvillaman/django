from __future__ import unicode_literals

from django.db import models

class MonthlyWeatherByCity(models.Model):
	month = models.IntegerField()
	boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
	houston_temp = models.DecimalField(max_digits=5, decimal_places=1)

	def __str__(self):
		return '%d' % (self.month)

	class Meta:
		ordering = ['month']

class DailyWeather(models.Model):
	month = models.IntegerField()
	day = models.IntegerField()
	temperature = models.DecimalField(max_digits=5, decimal_places=1)
	rainfall = models.DecimalField(max_digits=5, decimal_places=1)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=2)

	def __str__(self):
			return '%d' % (self.city)

class FedaralDays(models.Model):
	month = models.IntegerField()
	day = models.IntegerField()
	activity = models.CharField(max_length=100)

	def __str__(self):
		return '%s' % (self.activity)
		
	class Meta:
		ordering = ['month']

