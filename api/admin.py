from django.contrib import admin
from . import models

# Register your models here.
class SomeItemAdmin(admin.ModelAdmin):
	list_display = ('id','name','url')

admin.site.register(models.SomeItem, SomeItemAdmin)


