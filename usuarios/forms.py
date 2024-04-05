from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CreacionDeUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {llave : '' for llave in fields}

class EditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(label='Editar email')
    first_name = forms.CharField(label='Edite su nombre')
    last_name = forms.CharField(label='Edite su apellido')
    avatar = forms.ImageField(required=False)
    fecha_ingreso = forms.DateField(required=True)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar', 'fecha_ingreso']