from django.shortcuts import redirect, render, get_object_or_404
from sqlalchemy import distinct

from core.models import User
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django_postalcodes_mexico.models import PostalCode
from django.db.models import Q

# Create your views here.
def inicio(request):
    return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')


def servicios(request):
    busqueda = request.GET.get("buscar")
    codigos = PostalCode.objects.all()

    if busqueda:
        codigos = PostalCode.objects.filter(
            Q(d_codigo__icontains = busqueda)
        ).distinct()
    return render(request, 'core/servicios.html', {'codigos': codigos})


def perfilEditar(request, username):

    usuario = get_object_or_404(User, username=username)

    data = {
     'form': CustomUserCreationForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="inicio")
        data['form'] =  formulario
    return render(request, 'core/perfil.html', data)



def registroUsuario(request):  
    busqueda = request.GET.get("buscar")
    codigos = PostalCode.objects.all()

    if busqueda:
        codigos = PostalCode.objects.filter(
            Q(d_codigo__icontains = busqueda)
        ).distinct()

    data = {
     'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario =  CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password =  formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "registrado correctamente")
            #redirigir a inicio
            return redirect(to="inicio")
        data["form"] = formulario

    
        
    return render(request, 'registration/registro.html', data , {'codigos': codigos}) 
    

    
def prueba(request):
    return render(request, 'registration/prueba.html')