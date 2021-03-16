from django.conf.urls import url, include
from apps.Mascotas.views import index, mascota_list

urlpatterns= [
  url(r'^$', index, name='index'),
  url(r'^listar$', mascota_list, name='mascota_listar'),
]