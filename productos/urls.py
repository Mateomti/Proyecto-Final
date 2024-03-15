from django.contrib import admin
from django.urls import path
from productos import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/registrar/', views.RegistrarProducto.as_view(), name='registrar'),
    path('productos/listado/', views.Listado.as_view(), name='listado'),
    path('productos/<int:pk>/', views.Detalle.as_view(), name='detalle'),
    path('productos/<int:pk>/eliminar/', views.Eliminar.as_view(), name='eliminar'),
    path('productos/<int:pk>/editar/', views.Editar.as_view(), name='editar'),
    
    
    
]