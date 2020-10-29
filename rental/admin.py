from django.contrib import admin

# Register your models here.

from .models import Property
from .models import PropertyAdmin
from .models import Reservation
from .models import ReservationDate

admin.site.register(Property, PropertyAdmin)
admin.site.register(Reservation)
admin.site.register(ReservationDate)
