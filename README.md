# 🚀 API Django Rest Framework:

Este projeto é uma API desenvolvida com **Django Rest Framework**, estruturada para fornecer endpoints robustos, seguros e escaláveis.

📑 Descrição:

Esta API foi construída utilizando o framework Django e Django Rest Framework, oferecendo uma base sólida para desenvolvimento de sistemas backend, integração com aplicações frontend, serviços mobile ou outros sistemas.

O projeto está configurado para rodar dentro de um ambiente virtualizado usando **Vagrant**, garantindo isolamento do ambiente e facilidade na configuração.

---

⚙️ Tecnologias Utilizadas:

- 🐍 Python
- 🌐 Django
- 🔗 Django Rest Framework
- 📦 Vagrant (virtualização)
- 🔧 Virtualenv (ambiente isolado)

---

🚀 Como rodar o projeto:

1️⃣ Suba a máquina virtual com Vagrant:

bash : vagrant up

2️⃣ Acesse o ambiente Vagrant:
bash : vagrant ssh

3️⃣ Navegue até a pasta do projeto dentro do Vagrant:
bash : cd /vagrant

4️⃣ Ative o ambiente virtual (venv) dentro do Vagrant:
bash : source ~/envs/django_rest/venv/bin/activate

5️⃣ Rode o servidor Django:
bash : python manage.py runserver 0.0.0.0:8000

6️⃣ Acesse a API no navegador ou via ferramentas como Postman:
http://192.168.56.10:8000


