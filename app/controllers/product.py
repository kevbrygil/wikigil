from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from app.database import db
from app.models.product import Product
from app.schemas.product import ProductSchema
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

product = Blueprint('product', __name__)
 
schema = ProductSchema()

api = Api(product)

class CreateListProduct(Resource):
    
    def get(self):
        product_query = Product.query.all()
        results = schema.dump(product_query, many=True)['data']
        return results
 #Mapear las clases para los endpoints de la API
api.add_resource(CreateListProduct, '.json')
