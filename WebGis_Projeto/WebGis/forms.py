from django import forms
from django.db import models
from leaflet.forms.widgets import LeafletWidget
#from WebGis.models import Ocorrencia, TipoOcorrencia, RegistroOcorrencia
from WebGis.models import Categoria, Servico, RegistroServico

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['categoria', 'nome']

class RegistroServicoForm(forms.ModelForm):
    class Meta:
        model = RegistroServico
        fields = ['servico', 'local', 'foto']

    servico = forms.ModelChoiceField(queryset=Servico.objects.all(), required=True)
    local = forms.CharField(required=False)
    foto = forms.ImageField(required=False)
    latitude = forms.DecimalField(required=False, widget=forms.HiddenInput())
    longitude = forms.DecimalField(required=False, widget=forms.HiddenInput())
    ponto = forms.CharField(required=False, widget=forms.HiddenInput())

#class RegistroOcorrenciaForm(forms.Form):
#    oco_tipoOcorrencia = forms.CharField(max_length=50)
#    oco_nomeOcorrencia = forms.CharField(max_length=120)
#    oco_dataCadastro = forms.DateTimeField()
#    oco_dataRegistro = forms.DateTimeField()
#    oco_descricaoOcorrencia = forms.CharField(max_length=120)
#    latitude = forms.DecimalField()
#    longitude = forms.DecimalField()
'''
class InsereServicoForm(forms.ModelForm):
    oco_status = forms.BooleanField(
        label='Este serviço está ativo?',
        required=True
    )
    oco_descricaoOcorrencia = forms.CharField(
        label='Descrição do Serviço',
        required=False,
        widget = forms.Textarea
    )
    class Meta:
        # Modelo base
        model = Ocorrencia
        # Campos que estarão no form
        fields = [
                    'oco_tipoOcorrencia',
                    'oco_nomeOcorrencia'
        ]
        # Campos que não estarão no form
        exclude = [
                    'oco_ipAddress',
                    'oco_dataCadastro',
                    'oco_usuario'
        ]
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
'''
