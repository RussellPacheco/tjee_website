from dotenv import load_dotenv
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import create_engine
from sqlalchemy_utils import database_exists, create_database
from flask_cors import CORS
from whitenoise import WhiteNoise

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_CONNECTION = os.environ.get("DB_CONNECTION")
SQLALCHEMY_DATABASE = f'postgresql://{DB_CONNECTION}'

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root='static/')
app.url_map.strict_slashes = False
app.secret_key = os.environ.get("SECRET_TOKEN")
CORS(app, origins=["http://localhost:8080", "http://localhost:5000"])
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{DB_CONNECTION}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

###
#
# Creating the database
#
###

engine = create_engine(f"postgresql://{DB_CONNECTION}")
if not database_exists(engine.url):
    create_database(engine.url)

from app import routes, models
