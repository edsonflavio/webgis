from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime, date, time

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
