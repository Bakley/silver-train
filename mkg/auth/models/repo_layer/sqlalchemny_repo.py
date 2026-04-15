from extensions import db
from mkg.auth.schema.auth_schema import AuthSchema
from marshmallow import fields, validate, ValidationError
from flask import jsonify


auth = AuthSchema()
list_of_auth = AuthSchema(many=True)

class Crud:

    def create_data(self, obj):
        try:
            new_data = auth.load(
                obj
            )
        except ValidationError as err:
            return jsonify({
                "err": err.messages
            }), 422
        
        new_data.set_password(obj["password"])
        
        db.session.add(new_data)
        db.session.commit()

        return auth.dump(new_data)

