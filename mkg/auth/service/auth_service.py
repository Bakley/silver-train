from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

from mkg.auth.repo_layer.sqlalchemny_repo import Crud

from flask import jsonify


class AuthService():
    
    def __init__(self):
        self.repo = Crud()

    def register_user(self):
        pass

    def login_user(self, email, password):
        user = self.repo.get_by_email(email)


        if not user:
            return None, "No user with that email found, kindly go and register"
        
        if not check_password_hash(user.password, password):
            return None, "No user with that email found, kindly check the email or password"

        
        access_token = create_access_token(identity=str(user.id))
        refresh_token = create_refresh_token(identity=user.id)

        return {
            "access_token" : access_token,
            "refresh_token" : refresh_token,
            "user_detail" : {
                "username" : user.username,
                "id": user.id 
            }
        }, None
