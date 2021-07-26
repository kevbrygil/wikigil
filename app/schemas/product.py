from marshmallow_jsonapi import Schema, fields
from marshmallow import validate


class ProductSchema(Schema):

    id = fields.Integer(dump_only=True)   
    name = fields.String(required=True,
                        error_messages={'required': 'El nombre es requerido'},
                        validate=validate.Length(min=1, error='El nombre no debe estar en blanco'))

    sku = fields.String(required=True,
                        error_messages={'required': 'El SKU es requerido'},
                        validate=validate.Length(min=1, error='El SKU no debe estar en blanco'))

    price = fields.Float(required=True,
                        error_messages={'required': 'El precio es requerido'},
                        validate=validate.Length(min=1, error='El precio no debe estar en blanco'))

    size = fields.String(required=True,
                        error_messages={'required': 'El tamaño es requerido'},
                        validate=validate.Length(min=1, error='El tamaño no debe estar en blanco'))

    orders = fields.Nested('OrderSchema', many=True, dump_only=True, exclude=('product', ))

    shelves = fields.Nested('ShelfSchema', many=True, dump_only=True, exclude=('product', ))

 
    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = '/products'
        else:
            self_link = '/products/{}'.format(data['id'])
        return {'self': self_link}
    class Meta:
        type_ = 'product'