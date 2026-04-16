from flask import Blueprint, request, jsonify
from marshmallow import  ValidationError
from werkzeug.security import check_password_hash

from mkg.auth.models.auth_domain import Members
from mkg.auth.repo_layer.sqlalchemny_repo import Crud
from mkg.auth.service.auth_service import AuthService

auth_service = AuthService()

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
    if not body:
        return jsonify({"error": "Invalid Object"}), 400

    email = body.get("email")
    password = body.get("password")

    res, err = auth_service.login_user(email, password)

    if err:
        return jsonify({
        "message": "Login unsuccessful",
        "err": err
    }), 401

    return jsonify(res), 200
    