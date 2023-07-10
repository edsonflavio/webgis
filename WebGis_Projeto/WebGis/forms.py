from django import forms
from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis import forms
from django.contrib.gis.geos import Point
from leaflet.forms.widgets import LeafletWidget
from WebGis.models import Categoria, Servico, RegistroServico, Campus, User
from django_flatpickr.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from django.contrib.gis.db.models import PointField

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['nome', 'ponto_central']
        widgets = {
            'ponto': forms.HiddenInput(),
         }
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
        exclude = ('usuario', 'ip_origem')
        widgets = {
            'ponto': forms.HiddenInput(),
            "data_registro": DateTimePickerInput(),
        }
        fields = ['servico', 'campi', 'data_registro', 'descricao', 'ip_origem', 'foto', 'ponto']
        servico = forms.ModelChoiceField(queryset=Servico.objects.all(), required=True)
        campi   = forms.ModelChoiceField(queryset=Campus.objects.all(), required=True)
        data_registro = forms.DateTimeField(required=True, widget=DateTimePickerInput())
        descricao = forms.CharField(required=False, widget=forms.Textarea())
        ip_origem = forms.CharField(required=False, widget=forms.HiddenInput())
        foto    = forms.FileField(required=False, widget=forms.FileField())
        latitude  = forms.DecimalField(required=False, widget=forms.HiddenInput())
        longitude = forms.DecimalField(required=False, widget=forms.HiddenInput())
        endereco =  forms.DecimalField(required=False, widget=forms.HiddenInput())
        ponto = forms.PointField()