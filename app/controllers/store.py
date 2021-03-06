from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from app.database import db
from app.models.store import Store
from app.schemas.store import StoreSchema
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

store = Blueprint('store', __name__)
 
schema = StoreSchema()

api = Api(store)

class CreateListStore(Resource):
    
    def get(self):
        store_query = Store.query.all()
        results = schema.dump(store_query, many=True)['data']
        return results

    def post(self):
        raw_dict = request.get_json(force=True)
        try:
            schema.validate(raw_dict)
            request_dict = raw_dict['data']['attributes']

            store = Store(request_dict['name'], request_dict['address'], request_dict['latitude'], request_dict['longitude'])
            store.add(store)
            query = Store.query.get(store.id)
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
 
 
class GetUpdateDeleteStore(Resource):
    
    def get(self, id):
        store_query = Store.query.get_or_404(id)
        result = schema.dump(store_query)['data']
        return result
 
    def put(self, id):
        store = Store.query.get_or_404(id)
        raw_dict = request.get_json(force=True)
        try:
            schema.validate(raw_dict)
            request_dict = raw_dict['data']['attributes']
            for key, value in request_dict.items():
                setattr(store, key, value)
 
            store.update()
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
        store = Store.query.get_or_404(id)
        try:
            delete = store.delete(store)
            response = make_response()
            response.status_code = 204
            return response
 
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp


#Mapear las clases para los endpoints de la API
api.add_resource(CreateListStore, '.json')
api.add_resource(GetUpdateDeleteStore, '/<int:id>.json')