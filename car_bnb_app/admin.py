from django.contrib import admin
from .models import Person, Car, Rent
from django.contrib.sessions.models import Session
# Register your models here.


admin.site.register(Person)
admin.site.register(Car)
admin.site.register(Rent)
admin.site.register(Session)
