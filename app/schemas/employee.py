from marshmallow_jsonapi import Schema, fields
from marshmallow import validate

class EmployeeSchema(Schema):

    id = fields.Integer(dump_only=True)

    name = fields.String(required=True,
                        error_messages={'required': 'El nombre es requerido'},
                        validate=validate.Length(min=1, error='El nombre no debe estar en blanco'))
 
    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = '/employees'
        else:
            self_link = '/employees/{}'.format(data['id'])
        return {'employee': self_link}
    class Meta:
        type_ = 'employee'