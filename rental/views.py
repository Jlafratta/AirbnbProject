from django.shortcuts import render
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

    context = {
        'description': "Info de la casa",
        'property_id': property_id
    }
    return render(request, 'rental/propertyData.html', context)
