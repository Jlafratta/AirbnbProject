from django.shortcuts import render


# Create your views here.
def index(request):
    var = "Soy la variable enviada desde el controller"
    return render(request, 'rental/index.html', {'var': var})
