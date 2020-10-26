Requerimentos:
 Ter Python 3.7.9 (ou versão superior) instalado e adicionar no path

Requirements.txt:
 $ cd banco-website
 $ pip install -r requirements.txt

Fazendo o site funcionar:
 $ cd banco-website
 $ python manage.py runserver
 Acessar http://localhost:8000 no seu browser

Deploy para heroku:
 $ git clone https://github.com/GustavoDelaiOnzi/banco-website.git
 $ cd banco-website
 $ heroku create
 $ heroku addons:add memcachier:dev
 $ git push heroku master:master
 $ heroku open
 Para mais informações: https://www.treinaweb.com.br/blog/deploy-de-uma-aplicacao-django-no-heroku/

  
