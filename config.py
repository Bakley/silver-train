# I'll tell sqlalchemy where the db lives

class Config:
    # configure the folder the db is in

    SQLALCHEMY_DATABASE_URI = "sqlite:///library.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Prod(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://user:pass@localhost/library"
    