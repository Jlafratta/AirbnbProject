from django.db import models
from services.models import Service
from locations.models import City
from AirbnbProject import settings

# Create your models here.

from django.contrib.auth.models import AbstractUser
import datetime
import hashlib
from django.dispatch import receiver
import os


class User(AbstractUser):
    pass
    # class Meta:
    #    app_label = 'auth'


class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=450)
    capacity = models.IntegerField(default=0)
    dormitories = models.IntegerField(default=0)
    daily_price = models.FloatField(default=0.0)
    # FK que vincula con City
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="properties", null=True)
    short_description = models.CharField(max_length=70, default=None, null=True, blank=True)

    def __str__(self):
        return self.image.name


#  Eliminacion de los archivos de imagen una vez eliminada la property
def _delete_file(path):
    """ Deletes file from filesystem. """
    if os.path.isfile(path):
        os.remove(path)


@receiver(models.signals.post_delete, sender=PropertyImage)
def delete_file(sender, instance, *args, **kwargs):
    """ Deletes image files on `post_delete` """
    if instance.image:
        _delete_file(instance.image.path)


class Reservation(models.Model):

    total_price = models.FloatField(default=0.0)
    date = models.DateField(null=True)

    code = models.CharField(max_length=16, default='')
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')

    property = models.ForeignKey(Property, related_name='reservations', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"Titular: {self.first_name} {self.last_name}"

    def set_code(self):
        self.code = hashlib.md5(f"{self.email}{self.date}".encode("utf-8")).digest()    # hash de 16

    def set_date(self):
        self.date = datetime.datetime.now().date()


class ReservationDate(models.Model):
    date = models.DateField(null=True)
    property = models.ForeignKey(Property, related_name='reservation_dates', on_delete=models.CASCADE, null=True)
    reservation = models.ForeignKey(Reservation, related_name='r_dates', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"Reserva: {self.date}"






