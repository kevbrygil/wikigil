from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from app.database import db
from app.models.inventory import Inventory, InventorySchema
from app.models.product import Product,ProductSchema
from app.models.store import Store, StoreSchema
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
 

#Mapear las clases para los endpoints de la API
api.add_resource(CreateListInventory, '.json')
