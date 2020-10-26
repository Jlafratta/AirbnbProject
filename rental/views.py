from django.shortcuts import render, get_object_or_404
from .models import City
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


def property_data(request, property_id):
    prop = get_object_or_404(Property, pk=property_id)
    context = {
        'property': prop,
        'capacity': range(1, prop.capacity + 1)
    }
    return render(request, 'rental/propertyData.html', context)
