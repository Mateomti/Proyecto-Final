from django import forms
from productos.models import Productos

class CrearProducto(forms.ModelForm):
    marca = forms.CharField(label='Ingrese la marca', max_length=20)
    nombre = forms.CharField(label='Ingrese el nombre', max_length=20)
    fecha_vencimiento = forms.DateField(label='Ingrese la fecha de vencimiento')
    descripcion = forms.CharField(label='Ingrese alguna descripcion del producto', max_length=100)
    imagen = forms.ImageField(required=False)
    
    class Meta:
        model = Productos
        fields = ['marca', 'nombre', 'fecha_vencimiento', 'descripcion', 'imagen']
        help_texts = {llave : '' for llave in fields}

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(label='Ingrese un producto', max_length=20, required=False)