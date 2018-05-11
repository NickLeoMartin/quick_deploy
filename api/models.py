from django.db import models

# Create your models here.

class SomeItem(models.Model):
	""" Arbitrary Model """
	name = models.CharField(max_length=100,blank=True)
	description = models.CharField(max_length=300,blank=True)
	url = models.URLField(blank=True) 
	barcode = models.IntegerField(blank=True,null=True)



