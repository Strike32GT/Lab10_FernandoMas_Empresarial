from django.shortcuts import render
from .models import Producto
from django.http import JsonResponse

# Create your views here.
def lista_productos(request):
    productos=list(Producto.objects.values())
    return JsonResponse(productos, safe=False)