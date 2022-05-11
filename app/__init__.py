from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig, Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    # app.config.from_object(config_options[config_name])
    app.config.from_object(Config)



    # Initialising flask extensions
    bootstrap = Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Regestering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Regestering the auth bluprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    return app