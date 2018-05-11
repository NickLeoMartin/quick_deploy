from django.shortcuts import render
from rest_framework import generics
from . import serializers
from . import models
# Create your views here.

class SomeItemList(generics.ListAPIView):
	serializer_class = serializers.SomeItemSerializer
	queryset = models.SomeItem.objects.all()





