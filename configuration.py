import os

basedir = os.path.abspath(os.path.dirname(__file__))



class Config(object):

    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'el_xabr0n es la sena'

    #na versão web, utilizar diretório abaixo
    #mysql+pymysql://login_pythonanywhere:senhadb@lukedandrade.mysql.pythonanywhere-services.com/login@nome_do_banco
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False