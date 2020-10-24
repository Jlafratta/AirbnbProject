from django.shortcuts import render


# Create your views here.
def index(request):
    var = "Soy la variable enviada desde el controller"
    return render(request, 'rental/index.html', {'var': var})


def property_data(request, property_id):

    context = {
        'description': "Info de la casa",
        'property_id': property_id
    }
    return render(request, 'rental/propertyData.html', context)
