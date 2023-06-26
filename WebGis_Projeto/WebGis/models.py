from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TipoOcorrencias(models.Model):
    '''
        Tabela de Tipo de Ocorrências
    '''
    toc_tipoOcorrencia = models.CharField(max_length=50)
    toc_dataCadastro = models.DateTimeField(auto_now_add=True)
    toc_dataAlteracao = models.DateTimeField(auto_now=True)
    toc_ipAddress = models.GenericIPAddressField()
    toc_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

class Ocorrencia(models.Model):
    '''
        Tabela de Ocorrências
    '''
    oco_nomeOcorrencia = models.CharField(max_length=120)
    oco_dataCadastro = models.DateTimeField(auto_now_add=True)
    oco_dataAlteracao = models.DateTimeField(auto_now=True)
    oco_descricaoOcorrencia = models.CharField(max_length=120)
    oco_ipAddress = models.GenericIPAddressField()
