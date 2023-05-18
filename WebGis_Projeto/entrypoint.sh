#!/bin/sh

. /opt/venv/GIS_Project/bin/activate

./wait-for-database.sh ${PG_HOSTNAME}

python manage.py migrate --no-input
python manage.py collectstatic --no-input

#Bash
#if  [[ $PRIMEIRA_EXECUCAO == "sim" ]] ||  [[ $PRIMEIRA_EXECUCAO = "Sim" ]] ; then 
#sh
if [ "$PRIMEIRA_EXECUCAO" = 'sim' ] || [ "$PRIMEIRA_EXECUCAO" = 'Sim' ]; then 
	DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD \
		python manage.py createsuperuser \
		--username $DJANGO_SUPERUSER_USERNAME \
		--email $DJANGO_SUPERUSER_EMAIL --noinput
else
	echo "Usuário Admin do Django já existente, continunando somente!!"
	:
fi

gunicorn GIS_Project.wsgi:application --bind 0.0.0.0:8000
