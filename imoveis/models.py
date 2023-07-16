from django.db import models
from cloudinary.models import CloudinaryField

class Imoveis(models.Model):
    nome = models.CharField(max_length=250)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    choice_endereco = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    endereco_diferente = models.CharField(max_length=3, choices=choice_endereco)
    rua_medido = models.CharField(max_length=100, blank=True, null=True)
    bairro_medido = models.CharField(max_length=100, blank=True, null=True)
    frente = models.FloatField()
    fundo = models.FloatField()
    lado_direito = models.FloatField(null=True)  # Permitindo valor nulo
    lado_esquerdo = models.FloatField(null=True)  # Permitindo valor nulo
    area = models.FloatField()
    perimetro = models.FloatField()
    frente_com = models.CharField(max_length=100, blank=True, null=True)
    esquerda_com = models.CharField(max_length=100, blank=True, null=True)
    direita_com = models.CharField(max_length=100, blank=True, null=True)
    fundo_com = models.CharField(max_length=100, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    documento = models.CharField(max_length=255, null=True)
    primeiro_dono = models.CharField(max_length=100)
    data = models.DateField()
    num_documento = models.IntegerField() 
    choice_titulo = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    expedir_titulo = models.CharField(max_length=3, choices=choice_titulo, null=True)
    justificativa = models.TextField(blank=True, null=True)
    data_fiscalizacao = models.DateField()
    fiscal_1 = models.CharField(max_length=100, blank=True, null=True)
    fiscal_2 = models.CharField(max_length=100, blank=True, null=True)
    agente_medicao = models.CharField(max_length=100)
    
    foto_termo_medicao = CloudinaryField('image')