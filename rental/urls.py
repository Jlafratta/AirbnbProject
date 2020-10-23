from django.urls import path
from . import views

app_name = 'rental'
urlpatterns = [
    # url: /rental
    path('', views.index, name='index'),
]
