from django.urls import path
from usuarios.views import login, registro, perfil, editar, EditarContraseña
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'),name='logout'),
    path('registro/', registro, name='registro'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', editar, name='editar_perfil'),
    path('perfil/editar/contraseña/', EditarContraseña.as_view(), name='editar_contraseña')
    
]
