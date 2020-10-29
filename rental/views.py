from django.shortcuts import render, get_object_or_404
from locations.models import City
from .models import Property
from .models import Reservation
import datetime
from .models import ReservationDate
from .models import PropertyImage


# Create your views here.
def index(request):
    cities = City.objects.order_by('name')
    properties = Property.objects.all()
    context = {
        'cities': cities,
        'properties': properties
    }
    return render(request, 'rental/index.html', context)


def filter_by(request):

    if request.method == 'POST':
        properties = filter_properties(request.POST['city_id'], request.POST['capacity'], request.POST['date'])
    else:
        properties = Property.objects.all()     # Si hay falla en el metodo del formulario, no filtra

    context = {
        'cities': City.objects.order_by('name'),
        'properties': properties
    }
    return render(request, 'rental/index.html', context)


def filter_properties(city_id, capacity, date):  # Metodo de filtrado (falta que filtre por fecha)
    if city_id and capacity:
        return Property.objects.filter(city__id=city_id).filter(capacity=capacity)
    elif city_id:
        return Property.objects.filter(city__id=city_id)
    elif capacity:
        return Property.objects.filter(capacity=capacity)
    else:
        return Property.objects.all()   # Si no envia ningun filtro, devuelte todas


def property_data(request, property_id):
    prop = get_object_or_404(Property, pk=property_id)
    context = {
        'property': prop,
        'capacity': range(1, prop.capacity + 1)
    }
    return render(request, 'rental/propertyData.html', context)

def createReservation(request,propertyId):
    p= Property.objects.get(pk = propertyId )

    r = Reservation(date=datetime.datetime.now().date(),code = "xxxx", property=p)
    r.total = r.property.daily_price * request.POST['ReservationDateIds'].count()
    r.save()

    for reservationDateId in request.POST['ReservationDateIds'] :
        rd = ReservationDates.objects.get(pk = reservationDateId )
        rd.reserva = r
        rd.save()



