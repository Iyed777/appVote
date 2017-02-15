from __future__ import unicode_literals

from django.db import models

# Create your models here

class Member(models.Model):

	username = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	birth_date = models.DateField()
	registration = models.DateTimeField(auto_now_add=True)


	def __unicode__(self):
		return self.email