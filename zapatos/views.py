from django.shortcuts import render, get_object_or_404
from .models import Zapato
from decimal import Decimal

def vista_principal(request):
    zapato_id = None
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cantidad = request.POST.get('cantidad')
        proveedor = request.POST.get('proveedor')
        precio_total = request.POST.get('precio_total')

        if nombre and cantidad and proveedor and precio_total:
            cantidad = int(cantidad)  
            precio_total = Decimal(precio_total)  

            zapato = Zapato(nombre=nombre, cantidad=cantidad, proveedor=proveedor, precio_total=precio_total)
            zapato.save()
            zapato_id = zapato.id

    zapatos = Zapato.objects.all()
    return render(request, 'tienda/vista_principal.html', {'zapatos': zapatos, 'zapato_id': zapato_id})

def detalle_zapato(request, id):
    zapato = get_object_or_404(Zapato, id=id)
    return render(request, 'tienda/detalle_zapato.html', {'zapato': zapato})