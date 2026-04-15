from flask import Blueprint, request, jsonify
from marshmallow import  ValidationError

from mkg.auth.models.repo_layer.sqlalchemny_repo import Crud

auth_app = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_app.route("/register", methods=["POST"])
def register_a_new_user_record():
    body = request.get_json()

    if not body:
        return jsonify({
            "error": "Invalid Object"
        }), 400
     
    repo = Crud()

    try: 
        new_obj = repo.create_data(body)
        return new_obj
    except ValidationError as err:
        return jsonify({
                "err": err.messages
            }), 422


@auth_app.route("/login", methods=["POST"])
def login_a_user_record():
    body = request.get_json()
    
    error = validate_register(body)

    if error:
        return jsonify({
            "error": error
        })
    
    repo = Crud()
    
    new_obj = repo.create_data(body)

    return new_obj
    