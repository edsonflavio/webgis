from django import forms
from django.db import models
from django.contrib.gis.geos import Point
from leaflet.forms.widgets import LeafletWidget
from WebGis.models import Categoria, Servico, RegistroServico, Campus

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['nome', 'ponto_central']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['categoria', 'nome', 'descricao']

class RegistroServicoForm(forms.ModelForm):
    class Meta:
        model = RegistroServico
        fields = ['servico', 'usuario', 'campi', 'data_registro', 'descricao','ip_origem', 'foto', 'ponto']
    servico = forms.ModelChoiceField(queryset=Servico.objects.all(), required=True)
    campi = forms.ModelChoiceField(queryset=Campus.objects.all(), required=True)
    foto = forms.ImageField(required=False)
    latitude = forms.DecimalField(required=False, widget=forms.HiddenInput())
    longitude = forms.DecimalField(required=False, widget=forms.HiddenInput())

