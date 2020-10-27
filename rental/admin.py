from django.contrib import admin

# Register your models here.

from .models import City
from .models import Property
from .models import PropertyAdmin
from .models import Reservation

admin.site.register(City)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Reservation)
