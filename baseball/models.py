from django.db import models
from datetime import datetime    

class Calendario(models.Model):
	team = models.CharField('Team', max_length=30)
	contra = models.CharField('Contra', max_length=30)
	time = models.DateTimeField('Time', default=datetime.now, blank=True)
	date = models.DateTimeField('Date', default=datetime.now, blank=True)
	location = models.CharField('Location', max_length=40)
	# vaso = models.CharField('Vaso', max_length=40, default='vaso')

	def __str__(self):
		return self.team
