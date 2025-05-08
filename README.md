# API-Django-Rest-framework

mkdir -p ~/envs/django_rest
python3 -m venv ~/envs/django_rest/venv

-- rodar o projeto :

rode o conteiner - vagrant up
inicie o vagrant - vagrant ssh
entra na pasta do vagrant - cd /vagrant
ative a venv dentro do vagrant - source ~/envs/django_rest/venv/bin/activate

python manage.py runserver 0.0.0.0:8000
http://192.168.56.10:8000
