from django.shortcuts import render, get_object_or_404
from locations.models import City
from .models import Property
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

    context = {
        'cities': City.objects.order_by('name'),
        'properties': properties
    }
    return render(request, 'rental/index.html', context)


def filter_properties(city_id, capacity, date): # FALTARIA AGREGAR FILTRO X FECHA
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
    prop_img = PropertyImage.objects.filter(property__id=prop.id)
    context = {
        'property': prop,
        'property_images': prop_img,
        'capacity': range(1, prop.capacity + 1)
    }
    return render(request, 'rental/propertyData.html', context)





