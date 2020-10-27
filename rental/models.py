from django.db import models
from django.contrib import admin
from services.models import Service
from locations.models import City

# Create your models here.


class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    capacity = models.IntegerField(default=0)
    dormitories = models.IntegerField(default=0)
    daily_price = models.FloatField(default=0.0)
    # FK que vincula con City
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    total_price = models.FloatField(default=0.0)
    date = models.DateField(null=True)
    code = models.CharField(max_length=10, default='')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.code


class ReservationDate(models.Model):
    date = models.DateField(null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Reserva: {self.date}"


class ReservationDateInline(admin.TabularInline):
    model = ReservationDate
    fk_name = 'property'
    max_num = 7


class PropertyAdmin(admin.ModelAdmin):
    inlines = [ReservationDateInline, ]


