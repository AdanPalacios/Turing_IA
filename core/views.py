from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def servicios(request):
    return render(request, 'core/servicios.html')
