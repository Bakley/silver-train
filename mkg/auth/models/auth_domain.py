from extensions import db
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash


class Members(db.Model):
    __tablename__ = "members"

    id           = db.Column(db.Integer, primary_key=True)
    email        = db.Column(db.String(100))
    username     = db.Column(db.String(100))
    password     = db.Column(db.Text)
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)
    

    def set_password(self, value):
        self.password = generate_password_hash(value)

    def confirm_pass(self, value):
        return check_password_hash(self.password, value)

    