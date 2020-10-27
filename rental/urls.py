from django.urls import path
from . import views

app_name = 'rental'
urlpatterns = [
    # url: /rental
    path('', views.index, name='index'),
    path('results', views.filter_by, name='filter_by'),
    path('property/<int:property_id>', views.property_data, name='propertyData'),
]
