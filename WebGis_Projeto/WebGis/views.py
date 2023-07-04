# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.gis.geos import Point
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegistroOcorrenciaForm
from WebGis.models import Ocorrencia, TipoOcorrencia, RegistroOcorrencia
from datetime import datetime, date, time

class IndexTemplateView(TemplateView):
  template_name = "index.html"

class MapView(View):
    def get(self, request):
        form = RegistroOcorrenciaForm()
        ocorrencias = RegistroOcorrencia.objects.all()
        return render(request, 'mapa.html', {'form': form, 'Ocorrencias': ocorrencias})

class ListaServicos(ListView):
    template_name = "lista_servicos.html"
    model = Ocorrencia
    context_object_name = "servicos"

class ListaCategorias(ListView):
    template_name = "lista_categorias.html"
    model = TipoOcorrencia
    context_object_name = "categorias"

class ListaRegistros(ListView):
    template_name = "lista_registros.html"
    model = RegistroOcorrencia
    context_object_name = "registros"

class RegistroOcorrenciaView(View):
    def post(self, request):
        if request.user.is_authenticated:
            form = RegistroOcorrenciaForm(request.POST)
            if form.is_valid():
                nomeOcorrencia = form.cleaned_data['oco_nomeOcorrencia']
                tipoOcorrencia = form.cleaned_data['oco_tipoOcorrencia']
                dataCadastro = form.cleaned_data['oco_dataCadastro']
                dataRegistro = form.cleaned_data['oco_dataRegistro']
                descricaoOcorrencia = form.cleaned_data['oco_descricaoOcorrencia']
                proxy_habilitado = request.META["HTTP_X_NGINX_PROXY"]
                if proxy_habilitado == "true":
                    ipAddress = request.META["HTTP_X_REAL_IP"]
                else:
                    ipAddress = request.META["REMOTE_ADDR"]
                latitude = form.cleaned_data['latitude']
                longitude = form.cleaned_data['longitude']
                coordenadas = Point((longitude, latitude), srid=4326)
                registroOcorrencia = RegistroOcorrencia(
                    reg_Ocorrencia = tipoOcorrencia.set(),
                    reg_localOcorrencia=coordenadas,
                    reg_dataRegistro=dataRegistro,
                    reg_dataOcorrencia=dataCadastro,
                    reg_descricaoRegistro = descricaoOcorrencia,
                    reg_ipAddress = ipAddress,
                    reg_usuarioRegistro = request.user,
                    )
                registroOcorrencia.save()
                return redirect('mapa')
        else:
            return redirect('login')
        return render(request, 'mapa.html', {'form': form})

# class Ocorrencia(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('Hello, World')

#     def index(request):
#         # Prints client IP address: "12.34.56.78"
#         IP_Cliente = request.META["HTTP_X_FORWARDED_FOR"]
#         # Prints NGINX IP address: "127.0.0.1", ie. localhost
#         IP_Nginx = request.META["REMOTE_ADDR"]
#         Hoje = datetime.today()
#         Dia = Hoje.strftime("%d")
#         Mes = Hoje.strftime("%m")
#         Ano = Hoje.strftime("%Y")
#         Hora = Hoje.strftime("%H")
#         Min = Hoje.strftime("%M")
#         Seg = Hoje.strftime("%S")
#         ReturnMesg = f'Seja bem vindo - Seu IP é: <b> {IP_Cliente} </b>. <br> Seu acesso está sendo feito através do Servidor: <b> {IP_Nginx} </b>. <br> Hoje é dia: <b> {Dia}/{Mes}/{Ano} </b> e nosso horário é <b>{Hoje.strftime("%H:%M:%S")}h</b>.<br> Aqui começa seu WebGIS.'
#         return HttpResponse(ReturnMesg)

#     def home(request):
#         return render(request, 'home.html')

#     def have_proxy(proxy_habilitado:str)-> bool:
#         if proxy_habilitado == "true":
#             proxy = True
#         else:
#             proxy = False
#         return proxy
        
#     def create_ocorrencia(request):
#         '''
#             Permite o cadastro/registro de cada ocorrência 
#         '''
#         #ipRegistro = request.META["HTTP_X_FORWARDED_FOR"]
#         proxy_habilitado = request.META["HTTP_X_NGINX_PROXY"]
#         if have_proxy(proxy_habilitado):
#             ipRegistro = request.META["HTTP_X_REAL_IP"]
#         else:
#             ipRegistro = request.META["REMOTE_ADDR"]
#         ReturnMesg = f'Ocorrência <b>Criada<b> vinda do IP: <b> {ipRegistro} </b>. <br>'
#         return HttpResponse(ReturnMesg)

#     def list_ocorrencia(request):
#         '''
#             Lista as ocorrências registradas no sistema
#         '''
#         proxy_habilitado = request.META["HTTP_X_NGINX_PROXY"]
#         if have_proxy(proxy_habilitado):
#             ipRegistro = request.META["HTTP_X_REAL_IP"]
#         else:
#             ipRegistro = request.META["REMOTE_ADDR"]
#         dataRegistro = datetime.now()
#         ReturnMesg = f'Ocorrência <b>Criada<b> vinda do IP: <b> {ipRegistro} </b>. <br> Data da Criação: <b> {dataRegistro} <b><br>'
#         return HttpResponse(ReturnMesg)

#     def update_ocorrencia(request):
#         '''
#             Atualiza uma ocorrência registrada no sistema
#         '''
#         proxy_habilitado = request.META["HTTP_X_NGINX_PROXY"]
#         if have_proxy(proxy_habilitado):
#             ipRegistro = request.META["HTTP_X_REAL_IP"]
#         else:
#             ipRegistro = request.META["REMOTE_ADDR"]
#         dataRegistro = datetime.now()
#         ReturnMesg = f'Ocorrência <b>Atualizada<b> vinda do IP: <b> {ipRegistro} </b>.<br> Data da Atualização: <b> {dataRegistro} <b> <br>'
#         return HttpResponse(ReturnMesg)

#     def delete_ocorrencia(request):
#         '''
#             Apaga uma ocorrência registrada no sistema
#         '''
#         proxy_habilitado = request.META["HTTP_X_NGINX_PROXY"]
#         if have_proxy(proxy_habilitado):
#             ipRegistro = request.META["HTTP_X_REAL_IP"]
#         else:
#             ipRegistro = request.META["REMOTE_ADDR"]
#         dataRegistro = datetime.now()
#         ReturnMesg = f'Ocorrência <b>Eliminada<b> vinda do IP: <b> {ipRegistro} </b>.<br> Data da Eliminaação: <b> {dataRegistro} <b> <br>'
#         return HttpResponse(ReturnMesg)

#     def ocorrencia_form(request):
#         if request.method == 'POST':
#             latitude = request.POST['latitude']
#             longitude = request.POST['longitude']
#             coordenadas = Coordenadas(ponto='POINT({} {})'.format(longitude, latitude))
#             coordenadas.save()
#             return render(request, 'ocorrencias.html', {'coordenadas': coordenadas})
#         return render(request, 'ocorrencias.html')