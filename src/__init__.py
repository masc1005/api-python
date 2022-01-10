from flask import Flask
from src.database import connection, config_db
from .serializer import config as config_serial

from src.routes import bp

def create_app():
    app = Flask(__name__)

    config_db.init_app(app)
    connection.init_app(app)
    app.register_blueprint(bp)
    config_serial(app)

    return app
