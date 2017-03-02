from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.calendarListView, name='calendar_year'),
	url(r'^month/$', views.calendarMonthView, name='calendar_month'),
	url(r'^month/(?P<num>\d+)/$', views.day_calendarMonthView, name='calendar_month_day'),
	url(r'^(?P<month_game>\d+)/$', views.calendarListView_month, name='games_in_month'),
	url(r'^(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)/(?P<game_id>\w+)/$', views.game_view, name='gameview'),
]