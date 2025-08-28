"""
URL configuration for Template project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from templatesApp1.views import desplegarTemplate
from templatesApp1.views import renderTemplate
from templatesApp1.views import infoUsuario
from templatesApp1.views import diccionario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('verTemplate1/', desplegarTemplate),
    path('verTemplate2/', renderTemplate),
    #path('verTemplate3/', infoUsuario),
    path('verTemplate3/', diccionario),
]
