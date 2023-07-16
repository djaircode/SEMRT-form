from django.shortcuts import render


def lista_imoveis(request):
    return render(request, 'lista_imoveis.html')


def cadastrar_imovel(request):
    return render(request, 'cadastrar_imovel.html')