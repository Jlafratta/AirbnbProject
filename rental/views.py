from django.shortcuts import render, get_object_or_404
from locations.models import City
from .models import Property
from .models import Reservation
import datetime
from .models import ReservationDate


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
    # Me traigo las reservation dates con fecha limitada al dia de hoy en adelante
    reservation_dates = ReservationDate.objects.filter(date__gte=datetime.datetime.now().date()).filter(property=prop)

    context = {
        'property': prop,
        'reservation_dates': reservation_dates
    }
    return render(request, 'rental/propertyData.html', context)


def check_reservation(request, property_id):
    p = Property.objects.get(pk=property_id)
    reservation_dates = request.POST.getlist('reservation_dates[]')

    nights = len(reservation_dates)
    price = p.daily_price * nights
    tax = price * 0.08
    total_price = float(tax + price)

    context = {
        'property': p,
        'nights': nights,
        'price': price,
        'tax': tax,
        'total_price': int(total_price),
        'reservation_dates': reservation_dates
    }
    return render(request, 'rental/propertyData.html', context)


def create_reservation(request, property_id):

    p = Property.objects.get(pk=property_id)

    r = Reservation(date=datetime.datetime.now().date(), code="xxxx", property=p)
    r.save()

    reservation_dates = request.POST.getlist('reservation_dates[]')
    total = request.POST['total_price']

    for reservation_date in reservation_dates:
        # EL PROBLEMA ES PARSEAR BIEN EL DATE QUE EN EL ARRAY VIENE COMO '10 Nov. 2020'
        rd = ReservationDate.objects.get(date=datetime.datetime(2020, 11, 10), property=p)
        rd.reservation = r
        rd.save()

    # total = request.POST['total_price']

    r.total_price = total
    r.save()

    return index(request)
