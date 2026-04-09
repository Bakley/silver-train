# Marshmallow => convert of the python object to json

from app import seriliazer
from mkg.models import Author, Book

class AuthorSchema(seriliazer.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        load_instance = True
        include_fk = True


class BookSchema(seriliazer.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True
        include_fk = True
