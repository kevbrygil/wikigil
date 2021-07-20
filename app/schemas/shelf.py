from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from app.schemas.store import StoreSchema

class ShelfSchema(Schema):
 
    not_blank = validate.Length(min=1, error='Los campos no deben estar en blanco')

    id = fields.Integer(dump_only=True)
    name = fields.String(validate=not_blank)
    capacity = fields.Integer()
    latitude = fields.String()
    longitude = fields.String()

    storeid = fields.Integer()
    store = fields.Nested(StoreSchema)

    def get_top_level_links(self, data, many):
        if many:
            self_link = '/shelfs'
        else:
            self_link = '/shelfs/{}'.format(data['id'])
        return {'self': self_link}
    class Meta:
        type_ = 'shelf'