import os

class Config:
    SECRET_KEY = 'teeest'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('PASSWORD_EMAIL')

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '154647572'
    MYSQL_DB = 'academia_jam2023'


config = {
    'development': DevelopmentConfig
}
