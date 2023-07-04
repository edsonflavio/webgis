from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.

class TipoOcorrencia(models.Model):
    '''
        Tabela de Tipo de Ocorrências
    '''
    toc_usuario = models.ForeignKey(User, verbose_name="Usuário", on_delete=models.CASCADE)
    toc_tipoOcorrencia = models.CharField(max_length=50, verbose_name="Categoria do Reporte", help_text="Categoria na qual o Reporte será classificado", unique=True, db_index=True)
    toc_descOcorrencia = models.CharField(max_length=250, verbose_name="Descrição da Categoria", help_text="Descrição sucinta da Categoria")
    toc_dataCadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro", help_text="Data na qual houve o Cadastro da Categoria")
    toc_dataAlteracao = models.DateTimeField(auto_now=True, verbose_name="Data da Alteração", help_text="Data em que ocorreu a última alteração da Categoria")
    toc_ipAddress = models.GenericIPAddressField(verbose_name="Endereço IP", help_text="Endereço IP do Usuário que efetuou o Cadastro ou Alteração")
    objetos = models.Manager()
    class Meta:
        db_table = 'TipoOcorrencia'
    def __str__(self):
        return self.toc_tipoOcorrencia

class Ocorrencia(models.Model):
    '''
        Tabela de Ocorrências
    '''
    oco_usuario = models.ForeignKey(User, verbose_name="Usuário", help_text="Usuário que cadastrou ou alterou um Serviço" , on_delete=models.CASCADE)
    oco_tipoOcorrencia = models.ForeignKey(TipoOcorrencia, verbose_name="Categoria", help_text="Nome da Categoria que o Serviço se enquadra", on_delete=models.CASCADE)
    oco_nomeOcorrencia = models.CharField(max_length=120, verbose_name="Nome do Serviço", help_text="Nome que identifica uma situação que será registrada", unique=True, db_index=True)
    oco_dataCadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data do Cadastro", help_text="Data do cadastro de determinado serviço")
    oco_dataAlteracao = models.DateTimeField(auto_now=True, verbose_name="Data da Alteração", help_text="Data em que foi alterado o cadastro do serviço")
    oco_descricaoOcorrencia = models.CharField(max_length=120, verbose_name="Descrição do Serviço", help_text="Descreva de forma clara e sucinta o serviço.")
    oco_ipAddress = models.GenericIPAddressField(verbose_name="Endereço IP", help_text="Endereço IP do usuário que efetuou cadastro ou a última alteração")
    oco_status = models.BooleanField(default=True, verbose_name="Status do Serviço", help_text="Indica se o serviço está ativo ou não")
    objetos = models.Manager()
    class Meta:
        db_table = 'Ocorrencia'
    def __str__(self):
        return self.oco_nomeOcorrencia
    
class RegistroOcorrencia(models.Model):
    '''
        Tabela onde serão registradas todas as ocorrências
    '''
    reg_Ocorrencia = models.ManyToManyField(Ocorrencia, verbose_name="Código do Serviço", help_text="Relação com a Tabela de Serviços")
    reg_usuarioRegistro = models.ForeignKey(User, on_delete=models.CASCADE)
    reg_ipAddress = models.GenericIPAddressField(help_text="Endereço IP", verbose_name="Endereço IP do Usuário", null=False)
    reg_dataRegistro = models.DateTimeField(auto_now=True, help_text="Data de Registro da Ocorrência", null=False, verbose_name="Data do Registro")
    reg_dataOcorrencia = models.DateTimeField(auto_now_add=True, help_text="Data efetiva da Ocorrência", null=False)
    reg_descricaoRegistro = models.TextField(max_length=500, help_text="Descreva clara e sucintamente seu Reporte", blank=False, verbose_name="Descrição do Registro")
    reg_localOcorrencia = models.PointField(srid=4326, help_text="Coordenadas Geográficas do local onde ocorreu seu Reporte", null=False, verbose_name="Coordenadas do Local")
    objetos = models.Manager()
    class Meta:
        db_table = 'RegistroOcorrencia'
    def __str__(self):
        return f'{self.id}'