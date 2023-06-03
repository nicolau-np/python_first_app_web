from django.shortcuts import render
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objectos.all()
    data = {'pessoas': pessoas}
    return render(request, 'web/home.html', data)

def sobre(request):
    return render(request, 'web/sobre.html')

def contacto(request):
    return render(request, 'web/contacto.html')

def registo(request):
    return render(request, 'web/user/registo.html')

def salvar(request):
    nome = request.POST['nome']
    genero = request.POST['genero']

    pessoa = Pessoa(nome=nome, genero=genero)
    pessoa.save()
    return render(request, 'web/user/registo.html')
