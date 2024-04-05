from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from productos.models import Productos
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from productos.forms import CrearProducto, BusquedaForm
from django.contrib.auth.decorators import login_required



# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

class Listado(ListView):
    model = Productos
    context_object_name = 'prod'
    template_name = "prod/listado.html"
    form_class = BusquedaForm
    
    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda')

        if busqueda:
            queryset = queryset.filter(nombre__icontains=busqueda)
        else:
            queryset = queryset.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(self.request.GET)
        return context


class RegistrarProducto(CreateView):
    model = Productos
    form_class = CrearProducto
    template_name = "prod/crear.html"
    success_url = reverse_lazy('listado')

class Eliminar(LoginRequiredMixin, DeleteView):
    model = Productos
    template_name = "prod/eliminar.html"
    success_url = reverse_lazy('listado')

class Editar(LoginRequiredMixin, UpdateView):
    model = Productos   
    template_name = "prod/editar.html"
    success_url = reverse_lazy('listado')
    fields = ['marca', 'nombre', 'fecha_vencimiento', 'descripcion', 'imagen']

class Detalle(DetailView):
    model = Productos
    template_name = "prod/detalle.html"



