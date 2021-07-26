#Mapear las clases para los endpoints de la API
from flask import Blueprint
from flask_restful import Api
from app.controllers.employee import ListEmployees, CreateEmployee, \
                                GetEmployeeById, UpdateEmployeeById, DeleteEmployeeById

employee = Blueprint('employee', __name__)
api = Api(employee)

api.add_resource(ListEmployees, '.json')
api.add_resource(CreateEmployee, '.json')
api.add_resource(GetEmployeeById, '/<int:id>.json')
api.add_resource(UpdateEmployeeById, '/<int:id>.json')
api.add_resource(DeleteEmployeeById, '/<int:id>.json')