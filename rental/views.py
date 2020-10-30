from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

from locations.models import City
from .models import Property
from .models import Reservation
from .models import ReservationDate


def home(request):  # Redirecciona a /rental al ingresar al index principal del proyecto
    return HttpResponseRedirect(reverse('rental:index'))


# Create your views here.
def index(request, error=''):
    cities = City.objects.order_by('name')
    properties = Property.objects.all()
    context = {
        'cities': cities,
        'properties': properties,
        'error': error
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
    if request.method == 'POST':
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


def confirm_reservation(request, property_id):
    return render(request, 'rental/confirm.html')


def create_reservation(request, property_id):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        p = Property.objects.get(pk=property_id)

        try:
            r = Reservation(property=p, first_name=first_name, last_name=last_name, email=email)
            r.set_code()
            r.set_date()
            r.save()

            reservation_dates = request.POST.getlist('reservation_dates[]')
            total = request.POST['total_price']

            for reservation_date in reservation_dates:
                # Manejo de fechas en formato 'dd/mm/YYYY'
                rd = ReservationDate.objects.get(date=datetime.datetime.strptime(reservation_date, "%d/%m/%Y").date(), property=p)
                if rd.reservation:
                    raise ValueError
                rd.reservation = r
                rd.save()

            r.total_price = total
            r.save()
        except ReservationDate.MultipleObjectsReturned:     # Esto vuela una vez que se limite el repetir fechas de reservation_dates
            return index(request, "Mas de una reserva con la misma fecha")
        except ValueError:
            return index(request, "Reserva ocupada")

    return HttpResponseRedirect(reverse('rental:index',))
    # Redirecciono para limpiar la url que q no se pueda refrescar el formulario
