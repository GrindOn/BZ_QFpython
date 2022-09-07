import os


class Config:
    DEBUG = True
    # mysql+pymysql://user:password@hostip:port/databasename
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/flaskblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    # secret_key
    SECRET_KEY = 'kdjklfjkd87384hjdhjh'
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_DIR = os.path.join(BASE_DIR,'static')
    TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
    UPLOAD_DIR = os.path.join(STATIC_DIR,'upload')

class DevelopmentConfig(Config):
    ENV = 'development'


class ProductionConfig(Config):
    ENV = 'production'
    DDEBUG = False
if __name__ == '__main__':
    print(Config.BASE_DIR)