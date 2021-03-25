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

    def post(self):
        raw_dict = request.get_json(force=True)
        try:
            schema.validate(raw_dict)
            request_dict = raw_dict['data']['attributes']

            product = Product(request_dict['name'], request_dict['sku'], request_dict['price'], request_dict['size'])
            product.add(product)
            query = Product.query.get(product.id)
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
 
 
class GetUpdateDeleteProduct(Resource):
    
    def get(self, id):
        product_query = Product.query.get_or_404(id)
        result = schema.dump(product_query)['data']
        return result
 
    def put(self, id):
        product = Product.query.get_or_404(id)
        raw_dict = request.get_json(force=True)
        try:
            schema.validate(raw_dict)
            request_dict = raw_dict['data']['attributes']
            for key, value in request_dict.items():
                setattr(product, key, value)
 
            product.update()
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
        product = Product.query.get_or_404(id)
        try:
            delete = product.delete(product)
            response = make_response()
            response.status_code = 204
            return response
 
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp

 #Mapear las clases para los endpoints de la API
api.add_resource(CreateListProduct, '.json')
api.add_resource(GetUpdateDeleteProduct, '/<int:id>.json')
