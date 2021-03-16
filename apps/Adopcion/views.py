from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_Adopcion(request):
  return HttpResponse("Soy la pagina principal de adopción")
