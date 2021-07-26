from marshmallow_jsonapi import Schema, fields
from marshmallow import validate, ValidationError, validates
from app.schemas.building import BuildingSchema
from app.schemas.product import ProductSchema
from app.schemas.employee import EmployeeSchema

class ShelfSchema(Schema):
    id = fields.Integer(dump_only=True)
    
    name = fields.String(required=True,
                        error_messages={'required': 'El nombre es requerido'},
                        validate=validate.Length(min=1, error='El nombre no debe estar en blanco'))

    maxCapacity = fields.Integer(required=True,
                        error_messages={'required': 'La capacidad maxima es requerido'})

    availablesItems = fields.Integer(required=True,
                        error_messages={'required': 'La cantidad disponible es requerida'})

    latitude = fields.String(required=True,
                        error_messages={'required': 'La latitud es requerido'},
                        validate=validate.Length(min=1, error='La latitud no debe estar en blanco'))

    longitude = fields.String(required=True,
                        error_messages={'required': 'La longitud es requerido'},
                        validate=validate.Length(min=1, error='La longitud no debe estar en blanco'))

    employeeId = fields.Integer(required=True,
                        error_messages={'required': 'El personal es requerido'})

    productId = fields.Integer(required=True,
                        error_messages={'required': 'El producto es requerido'})

    buildingId = fields.Integer(required=True,
                        error_messages={'required': 'El almacen es requerido'})

    employee = fields.Nested(EmployeeSchema, dump_only=True)
    product = fields.Nested(ProductSchema, exclude=('chelves',), dump_only=True)
    building = fields.Nested(BuildingSchema, exclude=('chelves',), dump_only=True)

    @validates('maxCapacity')
    def validateMaxCapacity(self, value):
        if value < 0:
            raise ValidationError('La capacidad máxima no puede ser un número negativo')

    @validates('availablesItems')
    def validateavailablesItems(self, value):
        if value < 0:
            raise ValidationError('La cantidad de articulos disponibles no puede ser un número negativo')

    def get_top_level_links(self, data, many):
        if many:
            self_link = '/shelves'
        else:
            self_link = '/shelves/{}'.format(data['id'])
        return {'self': self_link}
    class Meta:
        type_ = 'shelf'