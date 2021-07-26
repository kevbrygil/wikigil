from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from app.models.building import BuildingCategory

class BuildingSchema(Schema):
    id = fields.Integer(dump_only=True)

    name = fields.String(required=True,
                        error_messages={'required': 'El nombre es requerido'},
                        validate=validate.Length(min=1, error='El nombre no debe estar en blanco'))

    address = fields.String(required=True,
                        error_messages={'required': 'La dirección es requerida'},
                        validate=validate.Length(min=1, error='La dirección no debe estar en blanco'))

    latitude = fields.String(required=True,
                        error_messages={'required': 'La latitud es requerida'},
                        validate=validate.Length(min=1, error='La latitud no debe estar en blanco'))

    longitude = fields.String(required=True,
                        error_messages={'required': 'La longitud es requerida'},
                        validate=validate.Length(min=1, error='La longitud no debe estar en blanco'))

    category = fields.Integer(required=True,
                        error_messages={'required': 'La categoría es requerida'},
                        validate=validate.OneOf(list(map(int, BuildingCategory))))

    shelves = fields.Nested('ShelfSchema', many=True, dump_only=True, exclude=('building', ))

    orders = fields.Nested('OrderSchema', many=True, dump_only=True, exclude=('building', ))

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = '/buildings'
        else:
            self_link = '/buildings/{}'.format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'building'
