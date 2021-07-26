from marshmallow_jsonapi import Schema, fields
from marshmallow import validate, ValidationError, validates
from app.schemas.building import BuildingSchema
from app.schemas.product import ProductSchema
from app.schemas.employee import EmployeeSchema

class OrderSchema(Schema):
    id = fields.Integer(dump_only=True)   
    name = fields.String(required=True,
                        error_messages={'required': 'El nombre es requerido'},
                        validate=validate.Length(min=1, error='El nombre no debe estar en blanco'))

    stockCount = fields.Integer(required=True,
                        error_messages={'required': 'La cantidad es requerida'})

    orderDate = fields.DateTime(dump_only=True)

    employeeId = fields.Integer(required=True,
                        error_messages={'required': 'El personal es requerido'})

    productId = fields.Integer(required=True,
                        error_messages={'required': 'El producto es requerido'})

    buildingId = fields.Integer(required=True,
                        error_messages={'required': 'La tienda es requerida'})

    employee = fields.Nested(EmployeeSchema, dump_only=True)
    product = fields.Nested(ProductSchema(exclude=('orders',)), dump_only=True)
    building = fields.Nested(BuildingSchema(exclude=('orders',)), dump_only=True)

    @validates('maxCapacity')
    def validateMaxCapacity(self, value):
        if value < 0:
            raise ValidationError('La capacidad máxima no puede ser un número negativo')

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = '/orders'
        else:
            self_link = '/orders/{}'.format(data['id'])
        return {'self': self_link}
    class Meta:
        type_ = 'order'