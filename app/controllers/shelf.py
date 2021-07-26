from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from app.database import db
from app.models.shelf import Shelf
from app.schemas.shelf import ShelfSchema
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

shelf = Blueprint('shelf', __name__)
 
schema = ShelfSchema()

api = Api(shelf)

class ListShelves(Resource):
    def get(self):
        shelfQuery = Shelf.query.all()
        results = schema.dump(shelfQuery, many=True)
        return results

class CreateShelf(Resource):
    def post(self):
        requestShelf = request.get_json(force=True)
        try:
            schema.validate(requestShelf)
            request_dict = schema.load(requestShelf)

            shelf = Shelf(request_dict['name'],
                          request_dict['maxCapacity'],
                          request_dict['availablesItems'],
                          request_dict['latitude'],
                          request_dict['longitude'],
                          request_dict['employeeId'],
                          request_dict['productId'],
                          request_dict['buildingId'])

            shelf.add(shelf)
            query = Shelf.query.get(shelf.id)
            results = schema.dump(query)
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

class GetShelfById(Resource):
    def get(self, id):
        shelf_query = Shelf.query.get_or_404(id)
        result = schema.dump(shelf_query)
        return result

class UpdateShelfById(Resource):
    def put(self, id):
        shelf = Shelf.query.get_or_404(id)
        requestShelf = request.get_json(force=True)
        try:
            schema.validate(requestShelf)
            shelfDict = schema.load(requestShelf)
            for key, value in shelfDict.items():
                setattr(shelf, key, value)
            shelf.update()
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

class DeleteShelfById(Resource):
    def delete(self, id):
        shelf = Shelf.query.get_or_404(id)
        try:
            shelf.delete(shelf)
            response = make_response()
            response.status_code = 204
            return response
 
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp