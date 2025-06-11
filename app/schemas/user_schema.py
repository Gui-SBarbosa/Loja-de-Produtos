from marshmallow import Schema, fields, validate

class UserRegisterSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=2))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=8))
    role = fields.Str(required=True, validate=validate.OneOf(["SELLER", "BUYER"]))


class UserLoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)



class UserResponseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    email = fields.Email()
    role = fields.Method("get_role")
    createdAt = fields.DateTime(dump_only=True)

    def get_role(self, obj):
        return obj.role.value
