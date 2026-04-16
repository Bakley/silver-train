from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity


from ...utilities.validators.user_validators import validate_register, sanitize_register
from mkg.authors_app.models.sqlite_repo import Crud

author_app = Blueprint("authors", __name__, url_prefix="/api/authors")

@author_app.route("/", methods=["POST"])
@jwt_required()
def create_a_record():
    body = request.get_json()
    
    error = validate_register(body)

    if error:
        return jsonify({
            "error": error
        })
    
    repo = Crud()
    
    new_obj = repo.create_data(body)

    return new_obj
    