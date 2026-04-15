from extensions import db
from datetime import datetime


class Book(db.Model):
    __tablename__ = "books"
    
    id            = db.Column(db.Integer, primary_key=True)
    title         = db.Column(db.String(100), nullable=False)
    year_pub      = db.Column(db.String(80))
    genre         = db.Column(db.Text)
    price         = db.Column(db.Float, nullable=False)
    created_at    = db.Column(db.DateTime, default=datetime.utcnow)


    
    author_id = db.Column(db.Integer, 
                          db.ForeignKey("wasomi.id"),
                          nullable=False)
    wakanda = db.relationship(
        "Author",
        back_populates="wassabi"
    )