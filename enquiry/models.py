
from django.db import models


class Enquiry(models.Model):
	name = models.CharField(max_length=30, null=False)

	address = models.TextField(null=False, default='')

	contact = models.CharField(max_length=25, null=False, default='')
	email = models.CharField(max_length=25, null=False, default='')

	enquiry = models.TextField(null=False, default='')
	

	

	

	
	def __str__(self):
		return str(self.name)