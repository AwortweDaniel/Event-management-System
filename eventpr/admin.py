from django.contrib import admin
from .models import Event, Registration

# email= admin@gmail.com ;password= user1234
# Register your models here.
admin.site.register(Event)
admin.site.register(Registration)
