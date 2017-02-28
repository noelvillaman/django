from django.conf.urls import url
from . import views

app_name = 'People'
urlpatterns = [
	url(r'^$', views.index, name='people_home'),
    url(r'^(?P<pID>\d+)/$', views.details, name='details'),
    url(r'^(?P<pID>\d+)/$', views.details, name='person_form'),
]