from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config

# flask
app = Flask(__name__)
api = Api(app)

# db
engine = create_engine(config.Config.SQLALCHEMY_DATABASE_URI, echo=True, future=True)
session = sessionmaker(bind=engine)()

# swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'event_api'
    }
)
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

from src import routes
from src.database import models
