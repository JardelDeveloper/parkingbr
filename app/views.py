from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def sejaparceiro(request):
    return render(request, 'sejaparceiro.html')


def quemsomos(request):
    return render(request, 'quemsomos.html')


def cadastrocliente(request):
    return render(request, 'cadastrocliente.html')


def cadastrogestor(request):
    return render(request, 'cadastrogestor.html')
