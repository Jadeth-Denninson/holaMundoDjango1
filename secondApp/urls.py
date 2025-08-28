from django.contrib import admin
from django.urls import path
from secondApp.views import saludo

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('saludo/', saludo),
]