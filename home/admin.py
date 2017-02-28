from django.contrib import admin
from .models import MonthlyWeatherByCity, DailyWeather, FedaralDays

admin.site.register(MonthlyWeatherByCity)
admin.site.register(DailyWeather)
admin.site.register(FedaralDays)
