from django.conf.urls import url
from apps.Adopcion.views import index_Adopcion

urlpatterns = [
  url(r'^$', index_Adopcion), 
]