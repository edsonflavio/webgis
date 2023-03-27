from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    # Prints client IP address: "12.34.56.78"
    IP_Cliente = request.META["HTTP_X_FORWARDED_FOR"]
    # Prints NGINX IP address: "127.0.0.1", ie. localhost
    IP_Nginx = request.META["REMOTE_ADDR"]
    return HttpResponse(f'Seja bem vindo ' + IP_Cliente + ' Você está acessando via ' + IP_Nginx +'. Aqui começa seu WebGIS.')