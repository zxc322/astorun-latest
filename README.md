# astorun_2022
dev --v

пока только локально 
c директории с docker-compose.yml выполнить:

$ docker-compose up -d --build

в браузере "http://localhost:8000/"

миграции:
$ docker-compose exec web python manage.py migrate

создать админа:
$ docker-compose exec web python manage.py createsuperuser
