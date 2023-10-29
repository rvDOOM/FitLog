from django.contrib import admin

from .models import Session, Workout, Sets

# Register your models here.

admin.site.register(Session)
admin.site.register(Workout)
admin.site.register(Sets)
