# webgis
Modelos de imagens para desenvolvedores Django, utilizando Docker.

Como utilizar este repositório para inicializar seu projeto Django de desenvovimento voltado para WebGIS

# Clone este repositório para inicializar

$ mkdir -p ~/webgis
$ cd ~/webgis
$ git clone https://github.com/edsonflavio/webgis.git webgis
$ cd webgis/WebGIS_Projeto

# Edite o arquivo .env para satisfazer suas necessidades

$ vim .env

# Executar o projeto usando docker compose

$ chmod +x *.sh
$ ./start.sh

# Para parar o serviço

$ ./stop.sh

# Para destruir a infraestrutura - começa do zero

$ ./rebuild.sh




