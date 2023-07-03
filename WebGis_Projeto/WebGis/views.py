# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date, time
from WebGis.models import Ocorrencia, TipoOcorrencia, RegistroOcorrencia

def index(request):
    # Prints client IP address: "12.34.56.78"
    IP_Cliente = request.META["HTTP_X_FORWARDED_FOR"]
    # Prints NGINX IP address: "127.0.0.1", ie. localhost
    IP_Nginx = request.META["REMOTE_ADDR"]
    Hoje = datetime.today()
    Dia = Hoje.strftime("%d")
    Mes = Hoje.strftime("%m")
    Ano = Hoje.strftime("%Y")
    Hora = Hoje.strftime("%H")
    Min = Hoje.strftime("%M")
    Seg = Hoje.strftime("%S")
    ReturnMesg = f'Seja bem vindo - Seu IP é: <b> {IP_Cliente} </b>. <br> Seu acesso está sendo feito através do Servidor: <b> {IP_Nginx} </b>. <br> Hoje é dia: <b> {Dia}/{Mes}/{Ano} </b> e nosso horário é <b>{Hoje.strftime("%H:%M:%S")}h</b>.<br> Aqui começa seu WebGIS.'
    return HttpResponse(ReturnMesg)

def has_proxy(proxy_habilitado:str)-> bool:
    if proxy_habilitado == "true":
        proxy = True
    else:
        proxy = False
    return proxy

def create_ocorrencia(request):
    '''
        Permite o cadastro/registro de cada ocorrência 
    '''
    #ipRegistro = request.META["HTTP_X_FORWARDED_FOR"]
    proxy_habilitado = request.META["HTTP_X_NGINX_PROXY"]
    if has_proxy(proxy_habilitado):
        ipRegistro = request.META["HTTP_X_REAL_IP"]
    else:
        ipRegistro = request.META["REMOTE_ADDR"]
    ReturnMesg = f'Ocorrência <b>Criada<b> vinda do IP: <b> {ipRegistro} </b>. <br>'
    return HttpResponse(ReturnMesg)

def list_ocorrencia(request):
    '''
        Lista as ocorrências registradas no sistema
    '''
    proxy_habilitado = request.META["HTTP_X_NGINX_PROXY"]
    if has_proxy(proxy_habilitado):
        ipRegistro = request.META["HTTP_X_REAL_IP"]
    else:
        ipRegistro = request.META["REMOTE_ADDR"]
    dataRegistro = datetime.now()
    ReturnMesg = f'Ocorrência <b>Criada<b> vinda do IP: <b> {ipRegistro} </b>. <br> Data da Criação: <b> {dataRegistro} <b><br>'
    return HttpResponse(ReturnMesg)

def update_ocorrencia(request):
    '''
        Atualiza uma ocorrência registrada no sistema
    '''
    proxy_habilitado = request.META["HTTP_X_NGINX_PROXY"]
    if has_proxy(proxy_habilitado):
        ipRegistro = request.META["HTTP_X_REAL_IP"]
    else:
        ipRegistro = request.META["REMOTE_ADDR"]
    dataRegistro = datetime.now()
    ReturnMesg = f'Ocorrência <b>Atualizada<b> vinda do IP: <b> {ipRegistro} </b>.<br> Data da Atualização: <b> {dataRegistro} <b> <br>'
    return HttpResponse(ReturnMesg)

def delete_ocorrencia(request):
    '''
        Apaga uma ocorrência registrada no sistema
    '''
    proxy_habilitado = request.META["HTTP_X_NGINX_PROXY"]
    if has_proxy(proxy_habilitado):
        ipRegistro = request.META["HTTP_X_REAL_IP"]
    else:
        ipRegistro = request.META["REMOTE_ADDR"]
    dataRegistro = datetime.now()
    ReturnMesg = f'Ocorrência <b>Eliminada<b> vinda do IP: <b> {ipRegistro} </b>.<br> Data da Eliminaação: <b> {dataRegistro} <b> <br>'
    return HttpResponse(ReturnMesg)


def home(request):
    return render(request, 'home.html')

def ocorrencia_form(request):
    if request.method == 'POST':
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        coordenadas = Coordenadas(ponto='POINT({} {})'.format(longitude, latitude))
        coordenadas.save()
        return render(request, 'ocorrencias.html', {'coordenadas': coordenadas})
    return render(request, 'ocorrencias.html')