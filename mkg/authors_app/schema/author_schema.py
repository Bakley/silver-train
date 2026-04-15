from extensions import seriliazer
from mkg.authors_app.models.author_domain import Author

class AuthorSchema(seriliazer.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        load_instance = True


