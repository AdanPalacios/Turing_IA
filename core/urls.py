from django import views
from django.urls import path, include
from . import views
from django_postalcodes_mexico import urls as django_postalcodes_mexico_urls


urlpatterns= [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('registro/', views.registroUsuario, name='registro'),
    path('prueba/', views.prueba, name='prueba'),
    path('perfilEditar/<username>/', views.perfilEditar, name='perfilEditar'),

    path('api/', include(django_postalcodes_mexico_urls)),
]