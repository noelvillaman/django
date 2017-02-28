from django.conf.urls import url
from django.contrib.auth import views as login_views
from . import views

urlpatterns = [
	#post views
	#url(r'^login/$', views.user_login, name='login'),

	# login / logout urls
	url(r'^login/$', login_views.login, name='login'),
	url(r'^logout/$', login_views.logout, name='logout'),
	url(r'^logout-then-login/$', login_views.logout_then_login, name='logout_then_login'),
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^password-change/$', login_views.password_change, name='password_change'),
	url(r'^password-change/done/$', login_views.password_change_done, name='password_change_done'),
	url(r'^password-reset/$', login_views.password_reset, {'post_reset_redirect' : 'password-reset/done/'}, name='password_reset'),
	url(r'^password-reset/done/$', login_views.password_reset_done, name='password_reset_done'),
	url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', login_views.password_reset_confirm,
		name='password_reset_confirm'),
	url(r'^password-reset/complete/$', login_views.password_reset_complete, name='password_reset_complete'),
	url(r'^register/$', views.register, name='register'),
	url(r'^edit/$', views.edit, name='edit'),
]