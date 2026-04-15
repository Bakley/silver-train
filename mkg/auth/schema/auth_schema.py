from extensions import seriliazer
from mkg.auth.models.auth_domain import Members

from marshmallow import fields, validate, validates, ValidationError
import re

class AuthSchema(seriliazer.SQLAlchemyAutoSchema):
    class Meta:
        model = Members
        load_instance = True

    email = fields.Email(
        required = True,
        validate =  validate.Length(max=100)

    )
    username = fields.Str(
        required = True,
        validate =  validate.Length(min=2, max=100)

    )
    password = fields.Str(
        required = True,
        load_only = True,
        validate =  validate.Length(min=8)
    )
    created_at = fields.DateTime(
        dump_only = True
    )

    # @validates("email")
    # def validate_email(self, email_value):
    #     if "test.com" in email_value:
    #         raise ValidationError("No disposabale email allowed")
        
    # @validates("password")
    # def validate_password(self, value):
    #     if not re.search(r"[A-Z]", value):
    #         raise ValidationError("Password must contain at least one uppercase letter")
    #     if not re.search(r"[a-z]", value):
    #         raise ValidationError("Password must contain at least one lowercase letter")
    #     if not re.search(r"[0-9]", value):
    #         raise ValidationError("Password must contain at least one integer")
    #     if not re.search(r"[!@#$%^&*]", value):
    #         raise ValidationError("Password must contaion at least one special character (!@#$%^&*)")

