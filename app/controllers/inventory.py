from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from app.database import db
from app.models.inventory import Inventory
from app.schemas.inventory import InventorySchema
from app.models.product import Product
from app.schemas.product import ProductSchema
from app.models.store import Store
from app.schemas.store import StoreSchema
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

inventory = Blueprint('inventory', __name__)
 
schema = InventorySchema()

api = Api(inventory)

class CreateListInventory(Resource):
    
    def get(self):
        inventory_query = Inventory.query.all()
        results = schema.dump(inventory_query, many=True)['data']
        return results

    def post(self):
        raw_dict = request.get_json(force=True)
        try:
            schema.validate(raw_dict)
            request_dict = raw_dict['data']['attributes']

            inventory = Inventory(request_dict['name'], request_dict['stock'], request_dict['shelfcount'], request_dict['storeid'], request_dict['productid'], request_dict['shelfid'])
            inventory.add(inventory)
            query = Inventory.query.get(inventory.id)
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
 
 
class GetUpdateDeleteInventory(Resource):
    
    def get(self, id):
        inventory_query = Inventory.query.get_or_404(id)
        result = schema.dump(inventory_query)['data']
        return result
 
    def put(self, id):
        inventory = Inventory.query.get_or_404(id)
        raw_dict = request.get_json(force=True)
        try:
            schema.validate(raw_dict)
            request_dict = raw_dict['data']['attributes']
            for key, value in request_dict.items():
                setattr(inventory, key, value)
 
            inventory.update()
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
        inventory = Inventory.query.get_or_404(id)
        try:
            delete = inventory.delete(inventory)
            response = make_response()
            response.status_code = 204
            return response
 
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp

api.add_resource(CreateListInventory, '.json')
api.add_resource(GetUpdateDeleteInventory, '/<int:id>.json')
