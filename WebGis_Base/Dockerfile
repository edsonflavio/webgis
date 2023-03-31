FROM python:3.11.2-bullseye
ENV PROJECT=GIS_Project
ENV VIRTUAL_ENV_PATH=/opt/venv/$PROJECT
LABEL br.ufpr.image.authors="Edson Flavio de Souza <edson.flavio@ufpr.br>"
LABEL version="1.0"
LABEL description="Ambiente de desenvolvimento Django com Postgis"
LABEL vendor="Universidade Federal do Parana \
            Agencia de Tecnologia da Informação\
            Coordenação de Serviços e Infraestrutura"
#Define o diretorio de trabalho do projeto
WORKDIR /code
#Atualiza o pip e instala as dependencias do projeto
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y postgresql-client \
                   binutils \
                   libproj-dev \
                   gdal-bin \
                   gdal-data \
                   python3-gdal \
                   postgis && \
    apt autoremove -y
RUN pwd && mkdir -p $VIRTUAL_ENV_PATH && ls -la $VIRTUAL_ENV_PATH && \
    python3 -m venv $VIRTUAL_ENV_PATH && \
    ls -la $VIRTUAL_ENV_PATH && \
    . $VIRTUAL_ENV_PATH/bin/activate && \
    pip install --upgrade pip
