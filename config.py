import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = '12345'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mariga:password@localhost/pitch4'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = "DATABASE_URL"


class DevConfig(Config):
    

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    # 'test': TestConfig

}