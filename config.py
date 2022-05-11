import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = '12345'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mariga:password@localhost/pitch4'


    # #email configurations
    # MAIL_SERVER ='smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = 'aizakmariga@gmail.com'
    # MAIL_PASSWORD = '@temporarypassword1234'

class ProdConfig(Config):
    pass

# class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mariga:password@localhost/_test'



class DevConfig(Config):
    

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    # 'test': TestConfig

}