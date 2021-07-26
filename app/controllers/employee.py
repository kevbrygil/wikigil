from flask import request, jsonify, make_response
from flask_restful import Resource
from app.database import db
from app.models.employee import Employee
from app.schemas.employee import EmployeeSchema
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

schema = EmployeeSchema()

class ListEmployees(Resource):
    def get(self):
        employeeQuery = Employee.query.all()
        results = schema.dump(employeeQuery, many=True)
        return results

class CreateEmployee(Resource):
    def post(self):
        requestEmployee = request.get_json(force=True)
        try:
            schema.validate(requestEmployee)
            employeeDict = schema.load(requestEmployee)

            employee = Employee(employeeDict['name'],
                                employeeDict['sku'],
                                employeeDict['price'],
                                employeeDict['size'])
            employee.add(employee)
            results = schema.dump(employee)
            return results, 201
 
        except ValidationError as err:
            resp = jsonify({"error": err.messages})
            resp.status_code = 403
            return resp
 
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 403
            return resp

class GetEmployeeById(Resource):
    def get(self, id):
        employeeQuery = Employee.query.get_or_404(id)
        result = schema.dump(employeeQuery)
        return result

class UpdateEmployeeById(Resource):
    def put(self, id):
        employee = Employee.query.get_or_404(id)
        requestEmployee = request.get_json(force=True)
        try:
            schema.validate(requestEmployee)
            employeeDict = schema.load(requestEmployee)
            for key, value in employeeDict.items():
                setattr(employee, key, value)
 
            employee.update()
            return self.get(id)
 
        except ValidationError as err:
            resp = jsonify({"error": err.messages})
            resp.status_code = 401
            return resp
 
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp

class DeleteEmployeeById(Resource):
    def delete(self, id):
        employee = Employee.query.get_or_404(id)
        try:
            employee.delete(employee)
            response = make_response()
            response.status_code = 204
            return response
 
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp
