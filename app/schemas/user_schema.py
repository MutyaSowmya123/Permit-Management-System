from marshmallow import Schema, fields, validate, ValidationError
from werkzeug.security import generate_password_hash

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3, max=80))
    password = fields.Str(required=True, validate=validate.Length(min=6), load_only=True)
    role = fields.Str(validate=validate.OneOf(['user', 'admin']), missing='user')

    def make_user(self, data, **kwargs):
        data['password'] = generate_password_hash(data['password'])
        return data

user_schema = UserSchema()
users_schema = UserSchema(many=True)
