from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def funciona(request):
    return HttpResponse("Funciona")

def seisPerf(request):
    cuenta = 0
    lista = [] 
    n = 1

    while cuenta < 4:
        sum = 0
        for i in range(1, n):
            if (n % i == 0):
                sum += 1
        
        if sum == n:
            lista.append(n)
            cuenta += 1
        n += 1

    return HttpResponse("<h2> Seis perfectos </h2></br>" + str(lista))

def diccionario(request):
    Estructura = {}
    mon = True
    n = 10
    for i in range(1, 11):
        lista = []
        for j in range(i):
            lista.append(mon)
            mon = not mon
        Estructura["elemento" + str(n)] = lista
        n/= 10

    return HttpResponse(str(Estructura))

