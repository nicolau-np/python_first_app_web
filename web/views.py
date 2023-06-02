from django.shortcuts import render
from .models import Pessoa

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contacto(request):
    return render(request, 'contacto.html')

def registo(request):
    return render(request, 'user/registo.html')

def salvar(request):
    nome = request.POST['nome']
    genero = request.POST['genero']

    pessoa = Pessoa(nome=nome, genero=genero)
    pessoa.save()
    return render(request, 'user/registo.html')
