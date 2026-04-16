# I'll tell sqlalchemy where the db lives

class Config:
    # configure the folder the db is in

    SQLALCHEMY_DATABASE_URI = "sqlite:///library.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "paste-64-char-secret-here"
    JWT_ACCESS_TOKEN_EXPIRES = 300 # 5 min
    JWT_REFRESH_TOKEN_EXPIRES = 900 # 15 min


class Prod(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://user:pass@localhost/library"
    