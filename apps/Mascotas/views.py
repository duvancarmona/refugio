from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.Mascotas.models import Mascotas
from apps.Mascotas.form import mascotaform

# Create your views here.
def index(request):
  return HttpResponse("Esta es Mascotas")

def mascota_list(request):
  mascota=Mascotas.objects.all()
  contexto={'mascotas': mascota}
  return render(request, 'mascota/mascota_list.html', contexto)

def mascota_view(request):
  if request.method=='POST':
    form = mascotaform(request.POST)
    if form. is_valid():
      form.save()
      return redirect('mascotas: index') 