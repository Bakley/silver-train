# FLASK factory 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy() # database connection
seriliazer = Marshmallow()

def create_app_for_developemnt():
    MKG = Flask(__name__)
    MKG.config.from_object("config.Config")

    db.init_app(MKG)
    seriliazer.init_app(MKG)

    # register the model(tables) for sql_alchemy to see them

    # register the blueprints(endpoints)

    return MKG


