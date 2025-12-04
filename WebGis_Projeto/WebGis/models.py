from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis import admin
from django.utils import timezone
from django.http import HttpRequest, HttpResponse
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.geos import GEOSGeometry
from django.urls import reverse_lazy

class ReporteUsuario(models.Model):
    class Genero(models.TextChoices):
        MAS = 'M', _('Masculino')
        FEM = 'F', _('Feminino')
        OUT = 'O', _('Outro')

    def get_genero(self) -> Genero:
        # Get value from choices enum
        return self.Genero[self.genero]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genero = models.CharField(
        max_length=2,
        choices = Genero.choices,
        default = Genero.OUT,
        verbose_name = 'Gênero d(ao) Usuári(ao)',
        help_text = 'Informe com qual Gênero você se Identifica.',)
    aniversario = models.DateField(
        verbose_name='Data de Aniversario do Usuario',
        help_text='Informe a Data do Seu Aniversário',
        null=False,
        blank=True)

class UnidadeGestora(models.Model):
    usuario = models.OneToOneField(ReporteUsuario, verbose_name=_("usuarios_reporte"), on_delete=models.CASCADE)
    nome_ug = models.CharField(
        max_length=60,
        verbose_name='Nome da Unidade Gestora',
        help_text='Informe o Nome da Unidade Gestora')
    descricao = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Descrição da Unidade Gestora',
        help_text='Descreva sucintamente a respeitor desta Unidade Gestora'
    )

    def __str__(self):
        return self.nome_ug

'''
class Task(models.Model):
    class Meta:
        permissions = [
            ("change_task_status", "Pode Alterar o Status da Ocorrência"),
            ("close_task", "Pode Encerrar uma Ocorrência marcando como Finalizada"),
        ]
'''
class Categoria(models.Model):
    nome = models.CharField(
        max_length=40, 
        verbose_name='Nome da Categoria', 
        help_text='Informe o Nome da Categoria')
    descricao = models.TextField(
        max_length=200,
        null=True,
        blank=True, 
        verbose_name='Descrição da Categoria', 
        help_text='Descreva sucintamente esta Categoria')

    def __str__(self):
        return self.nome

class Servico(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(
        max_length=60,
        verbose_name='Nome do Serviço',
        help_text='Informe o Nome do Serviço')
    descricao = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Descrição do Serviço',
        help_text='Descreva sucintamente este serviço'
    )

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
            return reverse("servico", kwargs={"pk": self.id})

class Campus(models.Model):  
    class Meta:
        ordering = ["nome"]
        verbose_name = "Identifação do Campus da UFPR"
        verbose_name_plural = 'Campi'

    nome = models.CharField(
        verbose_name="Nome do Campus",
        help_text="Informe o Nome do Campus mais próximo",
        max_length=60, 
        null=False, 
        blank=False, 
        db_index=True)
    ponto_central = models.PointField(
        verbose_name="Centróide do Campus",
        null=True, 
        blank=False,
        srid=4326,
        geography=True)
    
    def __str__(self):
        return self.nome

class RegistroServico(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    campi   = models.ForeignKey(Campus, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=500, 
                                 help_text='Descreva sucintamente a sua demanda/ocorrência (até 500 caracteres)',
                                 verbose_name="Descreve a ocorrência",
                                 blank=True,
                                 null=True)
    ip_origem = models.GenericIPAddressField(
        help_text='Recebe o IP do Usuário', 
        verbose_name='Endereço IP do Usuário')
    data_registro = models.DateTimeField(
        default=timezone.now,
        help_text='Data e Hora do Registro da Ocorrência',
        verbose_name='Recebe o data e hora do Registro da Ocorrência')
    data_alteracao = models.DateTimeField(
        auto_now=True,
        help_text='Data e Hora da Alteração do registro da Ocorrência',
        verbose_name='Recebe o data e hora da Alteração do Registro da Ocorrência')
    ponto = models.PointField(
        null=True, 
        blank=True,
        srid=4326,
        verbose_name='Localização aproximada da Ocorrência',
        help_text='Recebe as coordenadas aproximadas da Ocorrência')
    foto = models.FileField(
        upload_to='fotos/', 
        null=True, 
        blank=True,
        verbose_name='Permite a inserção de uma Foto para Registro da Ocorrência',
        help_text='Foto da Ocorrência'
        )
    class Meta:
        verbose_name_plural = "registro_servicos"
        ordering = ["data_registro"]
        verbose_name = "Registro das Ocorrências"

    def __str__(self):
        return f'{self.servico}'
