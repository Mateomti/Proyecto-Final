from django.contrib import admin
from django.urls import path
from productos.views import inicio


urlpatterns = [
    path('', inicio, name='inicio'),
]