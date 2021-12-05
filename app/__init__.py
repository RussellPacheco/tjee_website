from dotenv import load_dotenv
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import create_engine
from sqlalchemy_utils import database_exists, create_database
from flask_cors import CORS

load_dotenv()