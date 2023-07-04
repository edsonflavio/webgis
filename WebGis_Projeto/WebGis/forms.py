from django import forms

class RegistroOcorrenciaForm(forms.Form):
    oco_tipoOcorrencia = forms.CharField(max_length=50)
    oco_nomeOcorrencia = forms.CharField(max_length=120)
    oco_dataCadastro = forms.DateTimeField()
    oco_dataRegistro = forms.DateTimeField()
    oco_descricaoOcorrencia = forms.CharField(max_length=120)
    latitude = forms.DecimalField()
    longitude = forms.DecimalField()
