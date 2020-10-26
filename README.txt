Requerimentos:
 Ter Python 3.7.9 (ou versão superior) instalado e adicionar no path

Requirements.txt:
 $ cd mysite
 $ pip install -r requirements.txt

Fazendo o site funcionar:
 $ cd mysite
 $ python manage.py runserver
 Acessar http://localhost:8000 no seu browser

Deploy para heroku:
 $ git clone https://github.com/GustavoDelaiOnzi/banco-website.git
 $ cd mysite
 $ heroku create
 $ git push heroku master:master
 $ heroku open
 Para mais informações: https://www.treinaweb.com.br/blog/deploy-de-uma-aplicacao-django-no-heroku/

Site online em: https://banco-website.herokuapp.com/

Para adicionar dados no banco de dados: 
 $ cd mysite
 $ python manage.py createsuperuser
 Acessar "http://localhost:8000/admin" com o login e senha criados

Arquivos HTML estão localizados em: mysite\banco\templates\banco\
Imagens, arquivos HTML e JavaScript: mysite\banco\static\banco\
