from django.conf.urls import url 
from . import views

app_name = 'home'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^contact/$', views.contact_view, name='contact2'),
    url(r'^reading/$', views.reading_view, name='reading'),
    url(r'^bigarray/$', views.bakedArray, name='bigarray'),
    url(r'^nombre/$', views.get_name, name='nombre'),
    url(r'^result/$', views.get_name, name='nombre_result'),
    url(r'^activity/$', views.month_list, name='activity'),
    url(r'^pie/$', views.view_chart, name='piechart'),
    url(r'^weather/$', views.weather_view, name='weatherchart'),
    url(r'^assignment4/$', views.assignment4, name='assignment4'),
]