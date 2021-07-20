from marshmallow_jsonapi import Schema, fields
from marshmallow import validate

class StoreSchema(Schema):
 
    not_blank = validate.Length(min=1, error='Los campos no deben estar en blanco')

    id = fields.Integer(dump_only=True)   
    name = fields.String(validate=not_blank)
    address = fields.String(validate=not_blank)
    latitude = fields.String()
    longitude = fields.String()

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = '/stores'
        else:
            self_link = '/stores/{}'.format(data['id'])
        return {'self': self_link}
    class Meta:
        type_ = 'store'