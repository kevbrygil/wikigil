from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from app.database import db
from app.models.shelf import Shelf
from app.schemas.shelf import ShelfSchema
from app.models.store import Store
from app.schemas.store import StoreSchema
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

shelf = Blueprint('shelf', __name__)
 
schema = ShelfSchema()

api = Api(shelf)

class CreateListShelf(Resource):
    
    def get(self):
        shelfQuery = Shelf.query.all()
        results = schema.dump(shelfQuery, many=True)['data']
        return results

    def post(self):
        raw_dict = request.get_json(force=True)
        try:
            schema.validate(raw_dict)
            request_dict = raw_dict['data']['attributes']

            shelf = Shelf(request_dict['name'], request_dict['capacity'], request_dict['latitude'], request_dict['longitude'], request_dict['storeid'])
            shelf.add(shelf)
            query = Shelf.query.get(shelf.id)
            results = schema.dump(query)['data']
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
 
 
class GetUpdateDeleteShelf(Resource):
    
    def get(self, id):
        shelf_query = Shelf.query.get_or_404(id)
        result = schema.dump(shelf_query)['data']
        return result
 
    def put(self, id):
        shelf = Shelf.query.get_or_404(id)
        raw_dict = request.get_json(force=True)
        try:
            schema.validate(raw_dict)
            request_dict = raw_dict['data']['attributes']
            for key, value in request_dict.items():
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
 
    def delete(self, id):
        shelf = Shelf.query.get_or_404(id)
        try:
            delete = shelf.delete(shelf)
            response = make_response()
            response.status_code = 204
            return response
 
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp

api.add_resource(CreateListShelf, '.json')
api.add_resource(GetUpdateDeleteShelf, '/<int:id>.json')
