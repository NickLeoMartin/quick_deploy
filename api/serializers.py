from rest_framework import serializers
from . import models


class SomeItemSerializer(serializers.ModelSerializer): 
	class Meta:
		model = models.SomeItem
		fields = ('name','description','url','barcode')
		



