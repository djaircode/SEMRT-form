from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .models import Imoveis
import cloudinary.uploader
from django.contrib import messages

def lista_imoveis(request):
    return render(request, 'lista_imoveis.html')


def cadastrar_imovel(request):
    if request.method == ("GET"):    
        return render(request, 'cadastrar_imovel.html')
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')

        endereco_diferente = request.POST.get('endereco_diferente')

        rua_medido = request.POST.get('rua_medido')
        bairro_medido = request.POST.get('bairro_medido')
        frente = request.POST.get('frente')
        fundo = request.POST.get('fundo')
        lado_direito = request.POST.get('lado_direito')
        lado_esquerdo = request.POST.get('lado_esquerdo')
        area = request.POST.get('area')
        perimetro = request.POST.get('perimetro')
        frente_com = request.POST.get('frente_com')
        esquerda_com = request.POST.get('esquerda_com')
        direita_com = request.POST.get('direita_com')
        fundo_com = request.POST.get('fundo_com')
        observacao = request.POST.get('observacao')


        documento = request.POST.getlist('documento')
        documento_select = ','.join(documento)
        

        primeiro_dono = request.POST.get('primeiro_dono')
        data = request.POST.get('data')
        # 
        num_documento = request.POST.get('num_documento')
        # 
        expedir_titulo = request.POST.get('expedir_titulo')

        justificativa = request.POST.get('justificativa')
        # 
        data_fiscalizacao = request.POST.get('dt_fiscalizacao')
        # 
        fiscal_1 = request.POST.get('fiscal_1')
        fiscal_2 = request.POST.get('fiscal_2')
        agente_medicao = request.POST.get('agente_medicao')
        
        foto_termo_medicao = request.FILES['foto_termo_medicao']
        termo_upload_foto = cloudinary.uploader.upload(foto_termo_medicao)
        termo_medicao = termo_upload_foto['url']


        imovel = Imoveis(
            nome = nome,
            rua = rua,
            bairro = bairro,
            endereco_diferente = endereco_diferente,
            rua_medido = rua_medido,
            bairro_medido = bairro_medido,
            frente = frente,
            fundo = fundo ,
            lado_direito = lado_direito,
            lado_esquerdo = lado_esquerdo,
            area = area,
            perimetro = perimetro,
            frente_com = frente_com,
            esquerda_com = esquerda_com,
            direita_com = direita_com,
            fundo_com = fundo_com,
            observacao = observacao,
            documento = documento_select,
            primeiro_dono = primeiro_dono,
            data = data,
            # 
            num_documento = num_documento,
            # 
            expedir_titulo = expedir_titulo,
            justificativa = justificativa,
            data_fiscalizacao = data_fiscalizacao,
            fiscal_1 = fiscal_1,
            fiscal_2 = fiscal_2,
            agente_medicao = agente_medicao,
            foto_termo_medicao = termo_medicao,
        )

        imovel.save()
        
        messages.add_message(request, messages.SUCCESS, 'Vendedor excluido')
        return redirect(reverse('lista_imoveis'))