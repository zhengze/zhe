import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    SECRET_KEY = '78b32ed2bbb83f84d3d067ce3463d2aa943c7609'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    
class TestingConfig(Config):
    DATABASE = os.path.join(basedir, 'test.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE
    USERNAME = 'admin'
    PASSWORD = '1234'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE = os.path.join(basedir, 'dev.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE
    USERNAME = 'admin'
    PASSWORD = '1234'

class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost:3306/blog?charset=utf8'
    

config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductConfig,
    'default': DevelopmentConfig,
}
