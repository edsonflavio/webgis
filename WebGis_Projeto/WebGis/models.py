from django.db import models
from django.contrib.gis.db import models

from django.contrib.auth.models import User

# Create your models here.

class TipoOcorrencia(models.Model):
    '''
        Tabela de Tipo de Ocorrências
    '''
    toc_usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default='admin')
    toc_tipoOcorrencia = models.CharField(max_length=50)
    toc_dataCadastro = models.DateTimeField(auto_now_add=True)
    toc_dataAlteracao = models.DateTimeField(auto_now=True)
    toc_ipAddress = models.GenericIPAddressField()
    class Meta:
        db_table = 'TipoOcorrencia'
    def __str__(self):
        return self.toc_tipoOcorrencia

class Ocorrencia(models.Model):
    '''
        Tabela de Ocorrências
    '''
    oco_usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    oco_tipoOcorrencia = models.ForeignKey(TipoOcorrencia, on_delete=models.CASCADE, null=False, default=1)
    oco_nomeOcorrencia = models.CharField(max_length=120)
    oco_dataCadastro = models.DateTimeField(auto_now_add=True)
    oco_dataAlteracao = models.DateTimeField(auto_now=True)
    oco_descricaoOcorrencia = models.CharField(max_length=120)
    oco_ipAddress = models.GenericIPAddressField()
    class Meta:
        db_table = 'Ocorrencia'
    def __str__(self):
        return self.oco_nomeOcorrencia
    

class RegistroOcorrencia(models.Model):
    '''
        Tabela onde serão registradas todas as ocorrências
    '''
    reg_Ocorrencia = models.ForeignKey(Ocorrencia, on_delete=models.CASCADE, null=False)
    reg_usuarioRegistro = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default='admin')
    reg_ipAddress = models.GenericIPAddressField()
    reg_dataRegistro = models.DateTimeField(auto_now=True)
    reg_dataOcorrencia = models.DateTimeField(auto_now=True)
    reg_descricaoRegistro = models.TextField(max_length=500)
    reg_localOcorrencia = models.PointField()
    reg_ipAddress = models.GenericIPAddressField()
    class Meta:
        db_table = 'RegistroOcorrencia'
    def __str__(self):
        return self.reg_Ocorrencia