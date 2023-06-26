FROM projeto_base:latest
#FROM efsouza/webgis:base_ufpr-latest 
ENV PROJECT=GIS_Project
ENV VIRTUAL_ENV_PATH=/opt/venv/$PROJECT
LABEL br.ufpr.image.authors="Edson Flavio de Souza <edson.flavio@ufpr.br>"
LABEL version="1.0"
LABEL description="Ambiente de desenvolvimento Django com Postgis"
LABEL vendor="Universidade Federal do Parana \
            Agencia de Tecnologia da Informação\
            Coordenação de Serviços e Infraestrutura"
#Copia o codigo para o container
COPY . /code/
#Define o diretorio de trabalho do projeto
WORKDIR /code
RUN . $VIRTUAL_ENV_PATH/bin/activate
#Expoe a porta 8000 para acesso externo
EXPOSE 8000
#Inicia o servidor Django
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["sh", "entrypoint.sh"]