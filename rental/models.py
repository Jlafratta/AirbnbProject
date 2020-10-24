from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100)


class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    capacity = models.IntegerField(default=0)
    daily_price = models.FloatField(default=0.0)
    # FK que vincula con City
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Reservation(models.Model):
    total_price = models.FloatField(default=0.0)


class ReservationDates(models.Model):
    date = models.DateField
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)


