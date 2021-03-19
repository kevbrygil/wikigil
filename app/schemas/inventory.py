from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from app.schemas.product import ProductSchema
from app.schemas.store import StoreSchema

class InventorySchema(Schema):
 
    not_blank = validate.Length(min=1, error='Los campos no deben estar en blanco')

    id = fields.Integer(dump_only=True)   
    name = fields.String(validate=not_blank)
    stockCount = fields.Integer() 
    
    productid = fields.Integer()
    storeid = fields.Integer()
    product = fields.Nested(ProductSchema)
    store = fields.Nested(StoreSchema)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/inventoryitems"
        else:
            self_link = "/inventoryitems/{}".format(data['id'])
        return {'self': self_link}
    class Meta:
        type_ = 'inventory'