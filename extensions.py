from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy() # database connection
seriliazer = Marshmallow()
mig = Migrate()
json_token = JWTManager()
