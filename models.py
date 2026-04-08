# SQLAlchemy models
# each class maps to database table name
# each attribute maps to a column

from app import db
from datetime import datetime

class Author(db.Model):
    __tablename__ = "authors"
    
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(100), nullable=False)
    nationality  = db.Column(db.String(80))
    bio          = db.Column(db.Text)
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)

    # relationships
    books = db.relationship("Book", cascade="all, delete-orphan", back_populates="author")


class Book(db.Model):
    __tablename__ = "books"
    
    id            = db.Column(db.Integer, primary_key=True)
    title         = db.Column(db.String(100), nullable=False)
    year_pub      = db.Column(db.String(80))
    genre         = db.Column(db.Text)
    created_at    = db.Column(db.DateTime, default=datetime.utcnow)

    "a book belongs to an author"
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"), nullable=False)
    author = db.relationship("Author", back_populates="books")
