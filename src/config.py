import os

class Config:
    SECRET_KEY = os.urandom(32)
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
    MYSQL_PASSWORD = '154647572' # 'root1234'  '154647572'
    MYSQL_DB = 'academia_jam2023'

class appConfig():
    def init(app):
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_PASSWORD'] = '154647572' # 'root1234' '154647572'
        app.config['MYSQL_DB'] = 'academia_jam2023'
        app.config['SECRET_KEY'] = "teeest"
config = {
    'development': DevelopmentConfig
}
