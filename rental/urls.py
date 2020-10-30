from django.urls import path
from . import views

app_name = 'rental'
urlpatterns = [
    # url: /rental
    path('', views.index, name='index'),
    # url: /results
    path('results', views.filter_by, name='filter_by'),
    # url: /property/1
    path('property/<int:property_id>', views.property_data, name='propertyData'),
    # url: /property/1/createReservation
    path('property/<int:property_id>/createReservation', views.create_reservation, name='createReservation'),
    # url: /property/1/check
    path('property/<int:property_id>/check', views.check_reservation, name='check_reservation'),

]
