from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import CreacionDeUsuario, EditarPerfil
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtras
def login(request):
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contrasenia)
            django_login(request, user)
            return redirect('inicio')
        
    return render(request, 'usuarios/login.html', {'formulario':formulario})

def registro(request):
    formulario = CreacionDeUsuario()
    if request.method == 'POST':
        formulario = CreacionDeUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    return render(request, 'usuarios/registro.html', {'formulario':formulario})

def perfil(request):
    return render(request, 'usuarios/perfil.html')

def editar(request):
    user = request.user
    datos_extras, _= DatosExtras.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        formulario = EditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            avatar = formulario.cleaned_data.get('avatar')
            if avatar:
                datos_extras.avatar = avatar
            datos_extras.save()
            formulario.save()
            return redirect('perfil')
    else:
        formulario = EditarPerfil(initial={'avatar':datos_extras.avatar}, instance=request.user)
        
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

class EditarContraseña(PasswordChangeView):
    template_name = 'usuarios/editar_contraseña.html'
    success_url = reverse_lazy('perfil')