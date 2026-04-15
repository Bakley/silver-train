from extensions import db
from datetime import datetime


class Author(db.Model):
    __tablename__ = "wasomi"

    id           = db.Column(db.Integer, primary_key=True)
    email        = db.Column(db.String(100))
    username     = db.Column(db.String(100))
    nationality  = db.Column(db.String(80))
    bio          = db.Column(db.Text)
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)

# relationship
    wassabi = db.relationship(
        "Book",
        cascade="all, delete-orphan",
        back_populates="wakanda")
    