from extensions import db
from mkg.authors_app.schema.author_schema import AuthorSchema
from marshmallow import fields, validate, ValidationError
from flask import jsonify


author = AuthorSchema()
list_of_authors = AuthorSchema(many=True)

class Crud:

    def create_data(self, obj):
        try:
            new_data = author.load(
                obj
            )
        except ValidationError as err:
            return jsonify({
                "err": err.messages
            }), 422
        
        db.session.add(new_data)
        db.session.commit()

        return author.dump(new_data)

