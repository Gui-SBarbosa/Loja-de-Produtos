from marshmallow import Schema, fields, validate

# Create
class ProductCreateSchema(Schema):
    name_product = fields.Str(required=True, validate=validate.Length(min=2))
    value = fields.Float(required=True, validate=validate.Range(min=0.01))
    description = fields.Str(required=True, validate=validate.Length(min=10))
    quantity = fields.Int(required=True, validate=validate.Range(min=1))

class ProductCreateResponse(Schema):
    id = fields.Int(dump_only=True)
    name_product = fields.Str()
    value = fields.Float()
    description = fields.Str()
    quantity = fields.Int()
    id_seller = fields.Int(dump_only=True)
    createdAt = fields.DateTime(dump_only=True)

# Update
class ProductUpdateSchema(Schema):
    name_product = fields.Str(validate=validate.Length(min=2))
    value = fields.Float(validate=validate.Range(min=0.01))
    description = fields.Str(validate=validate.Length(min=10))
    quantity = fields.Int(validate=validate.Range(min=1))

class ProductUpdateResponse(Schema):
    id = fields.Int(dump_only=True)
    name_product = fields.Str()
    value = fields.Float()
    description = fields.Str()
    quantity = fields.Int()
    updatedAt = fields.DateTime(dump_only=True)

# Details
class ProductDetailSchema(Schema):
    id = fields.Int(dump_only=True)
    name_product = fields.Str()
    value = fields.Float()
    description = fields.Str()
    quantity = fields.Int()
    seller_name = fields.Function(lambda obj: obj.seller.name if obj.seller else None)
    id_seller = fields.Int(dump_only=True)
    createdAt = fields.DateTime(dump_only=True)
    updatedAt = fields.DateTime(dump_only=True)
