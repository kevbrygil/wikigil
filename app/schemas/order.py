from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from app.schemas.product import ProductSchema
from app.schemas.store import StoreSchema
from app.schemas.shelf import ShelfSchema

class OrderSchema(Schema):
 
    not_blank = validate.Length(min=1, error='Los campos no deben estar en blanco')

    id = fields.Integer(dump_only=True)   
    name = fields.String(validate=not_blank)
    stock = fields.Integer() 
    shelfcount = fields.Integer() 
    
    productid = fields.Integer()
    storeid = fields.Integer()
    shelfid = fields.Integer()
    product = fields.Nested(ProductSchema)
    store = fields.Nested(StoreSchema)
    shelf = fields.Nested(ShelfSchema)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = '/orderitems'
        else:
            self_link = '/orderitems/{}'.format(data['id'])
        return {'self': self_link}
    class Meta:
        type_ = 'order'