from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    capacity = models.IntegerField(default=0)
    dormitories = models.IntegerField(default=0)
    daily_price = models.FloatField(default=0.0)
    # FK que vincula con City
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    total_price = models.FloatField(default=0.0)
    date = models.DateField
    code = models.CharField(max_length=10)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return self.total_price


class ReservationDates(models.Model):
    date = models.DateField
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.date

