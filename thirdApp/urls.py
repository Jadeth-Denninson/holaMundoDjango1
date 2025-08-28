from django.contrib import admin
from django.urls import path
from thirdApp.views import funciona, diccionario, seisPerf

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('funciona/', funciona),
    path('perfect/', seisPerf),
    path('diccionario/', diccionario),
]