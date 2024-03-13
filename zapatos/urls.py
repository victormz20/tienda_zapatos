from django.urls import path
from . import views

app_name = 'zapatos'

urlpatterns = [
    path('', views.vista_principal, name='vista_principal'),
    path('zapato/<int:id>', views.detalle_zapato, name='detalle_zapato'),
]