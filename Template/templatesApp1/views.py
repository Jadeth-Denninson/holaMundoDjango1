from django.shortcuts import render

def desplegarTemplate(request):
    return render(request, 'templatesApp1/ejemplo1.html')

def renderTemplate(request):
    data = {"nombre" : "Denninson"}
    return render(request, 'templatesApp1/ejemplo1.html', data)

def infoUsuario(request):
    data1 = {"id" : 123, "nombre" : "Clark Kent", "email" : "superman@jl.org"} 
    return render(request, 'templatesApp1/userinfotemplate.html', data1)

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

    return render(request, 'templateApp1/ejemplo1.html', {'datos': Estructura})