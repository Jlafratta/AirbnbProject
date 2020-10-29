from django.db import models
from django.contrib import admin
from services.models import Service
from locations.models import City

# Create your models here.


class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=450)
    capacity = models.IntegerField(default=0)
    dormitories = models.IntegerField(default=0)
    daily_price = models.FloatField(default=0.0)
    # FK que vincula con City
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, blank=True)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="properties", null=True)
    short_description = models.CharField(max_length=70, default=None, null=True, blank=True)

    def __str__(self):
        return self.image.name


class Reservation(models.Model):
    total_price = models.FloatField(default=0.0)
    date = models.DateField(null=True)
    code = models.CharField(max_length=10, default='')
    property = models.ForeignKey(Property, related_name='reservations', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.code


class ReservationDate(models.Model):
    date = models.DateField(null=True)
    property = models.ForeignKey(Property, related_name='reservation_dates', on_delete=models.CASCADE, null=True)
    reservation = models.ForeignKey(Reservation, related_name='r_dates', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Reserva: {self.date}"


class ReservationDateInline(admin.TabularInline):
    model = ReservationDate
    fk_name = 'property'
    max_num = 7


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    fk_name = 'property'
    max_num = 10


class PropertyAdmin(admin.ModelAdmin):
    inlines = [ReservationDateInline, PropertyImageInline, ]


