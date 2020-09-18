from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def sejaparceiro(request):
    return render(request, 'sejaparceiro.html')


def quemsomos(request):
    return render(request, 'quemsomos.html')


def cadastro(request):
    return render(request, 'cadastro.html')
