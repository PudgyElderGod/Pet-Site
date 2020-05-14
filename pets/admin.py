from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Pet)
admin.site.register(models.Appointment)