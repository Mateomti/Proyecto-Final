from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from productos.models import Productos
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin




# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

class Listado(ListView):
    model = Productos
    context_object_name = 'prod'
    template_name = "prod/listado.html"


class RegistrarProducto(CreateView):
    model = Productos
    template_name = "prod/crear.html"
    fields = ['marca', 'nombre', 'fecha_vencimiento', 'descripcion']
    success_url = reverse_lazy('listado')

class Eliminar(LoginRequiredMixin, DeleteView):
    model = Productos
    template_name = "prod/eliminar.html"
    success_url = reverse_lazy('listado')

class Editar(LoginRequiredMixin, UpdateView):
    model = Productos
    template_name = "prod/editar.html"
    success_url = reverse_lazy('listado')
    fields = ['marca', 'nombre', 'fecha_vencimiento', 'descripcion']

class Detalle(DetailView):
    model = Productos
    template_name = "prod/detalle.html"



