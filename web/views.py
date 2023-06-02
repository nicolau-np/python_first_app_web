from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contacto(request):
    return render(request, 'contacto.html')

def registo(request):
    return render(request, 'user/registo.html')
