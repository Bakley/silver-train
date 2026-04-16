# FLASK factory 
from flask import Flask
from extensions import db, seriliazer, mig, json_token

JWT_SECRET_KEY = "paste-64-char-secret-here-paste-64-char-secret-here-paste-64-char-secret-here"
JWT_ACCESS_TOKEN_EXPIRES = 300 # 5 min
JWT_REFRESH_TOKEN_EXPIRES = 900 # 15 min


def create_app_for_developemnt():
    MKG = Flask(__name__)
    MKG.config.from_object("config.Config")

    db.init_app(MKG)
    seriliazer.init_app(MKG)
    mig.init_app(MKG)
    json_token.init_app(MKG)

    # register the model(tables) for sql_alchemy to see them
    from mkg.auth.models.auth_domain import Members

    from mkg.authors_app.models.author_domain import Author
    from mkg.books_app.models.book_domain import Book

    # register the blueprints(endpoints)
    from mkg.authors_app.controllers.authors_routes import author_app
    MKG.register_blueprint(author_app)

    from mkg.auth.controllers.auth_routes import auth_app
    MKG.register_blueprint(auth_app)
    
    return MKG
