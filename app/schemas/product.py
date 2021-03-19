from marshmallow_jsonapi import Schema, fields
from marshmallow import validate

class ProductSchema(Schema):
 
    not_blank = validate.Length(min=1, error='Los campos no deben estar en blanco')
    not_zero = validate.Length(min=1, error='Los campos no deben estar en blanco')

    id = fields.Integer(dump_only=True)   
    sku = fields.String(validate=not_blank)
    price = fields.Decimal()
    size = fields.String(validate=not_blank)
 
    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/products"
        else:
            self_link = "/products/{}".format(data['id'])
        return {'self': self_link}
    class Meta:
        type_ = 'product'