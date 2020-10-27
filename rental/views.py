from django.shortcuts import render, get_object_or_404
from locations.models import City
from .models import Property


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

        if request.POST['city_id']:
            properties = Property.objects\
                .filter(city__id=request.POST['city_id'])

        else:
            properties = Property.objects.all()

    cities = City.objects.order_by('name')
    context = {
        'cities': cities,
        'properties': properties
    }
    return render(request, 'rental/index.html', context)


def property_data(request, property_id):
    prop = get_object_or_404(Property, pk=property_id)
    context = {
        'property': prop,
        'capacity': range(1, prop.capacity + 1)
    }
    return render(request, 'rental/propertyData.html', context)
