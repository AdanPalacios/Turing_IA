from django import forms

from core.models import User

from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'telefono', 'codigo_postal', 'pais', 'estado', 'municipio', 'localidad', 'colonia', 'calle']
        help_texts = {k:"" for k in fields}



    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-sm-9 text-secondary', 'placeholder' :'Usuario'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-sm-9 text-secondary', 'placeholder' :'nombre'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-sm-9 text-secondary', 'placeholder' :'apellido'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'col-sm-9 text-secondary', 'placeholder' :'correo'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'col-sm-9 text-secondary', 'placeholder' :'contrasena'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'col-sm-9 text-secondary', 'placeholder' :'repetir contrasena'}))
    
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-sm-9 text-secondary', 'placeholder' :'telefono'}))
    codigo_postal = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-sm-9 text-secondary', 'placeholder' :'codigo_postal','id' :'codigoPostal'}))
    pais = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-sm-9 text-secondary', 'placeholder' :'pais','id' :'pais'}))
    estado = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-sm-9 text-secondary', 'placeholder' :'estado','id' :'estado'}))
    municipio = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-sm-9 text-secondary', 'placeholder' :'municipio',  'id' :'municipio'}))
    localidad = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-sm-9 text-secondary', 'placeholder' :'localidad','id' :'localidad'}))
    colonia = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-sm-9 text-secondary', 'placeholder' :'colonia', 'id' :'colonia'}))
    calle = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-sm-9 text-secondary', 'placeholder' :'calle'}))
