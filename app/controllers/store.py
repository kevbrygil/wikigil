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
        store_query = store.query.all()
        results = schema.dump(store_query, many=True)['data']
        return results

#Mapear las clases para los endpoints de la API
api.add_resource(CreateListStore, '.json')
