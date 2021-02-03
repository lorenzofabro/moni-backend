docker-compose run django python moni/manage.py migrate
docker-compose run django python moni/manage.py loaddata initial_data.json