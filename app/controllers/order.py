from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from app.database import db
from app.models.order import Order
from app.schemas.order import OrderSchema
from app.models.product import Product
from app.schemas.product import ProductSchema
from app.models.store import Store
from app.schemas.store import StoreSchema
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

order = Blueprint('order', __name__)
 
schema = OrderSchema()

api = Api(order)

class CreateListOrder(Resource):
    
    def get(self):
        orderQuery = Order.query.all()
        results = schema.dump(orderQuery, many=True)
        return results

    def post(self):
        requestOrder = request.get_json(force=True)
        try:
            schema.validate(raw_dict)
            orderDict = schema.load(requestOrder)
            order = Order(orderDict['name'], 
                        orderDict['stock'], 
                        orderDict['shelfcount'], 
                        orderDict['storeid'], 
                        orderDict['productid'], 
                        orderDict['shelfid'])
            order.add(order)
            results = schema.dump(product)
            query = Order.query.get(order.id)
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
 
 
class GetUpdateDeleteOrder(Resource):
    
    def get(self, id):
        orderQuery = Order.query.get_or_404(id)
        result = schema.dump(orderQuery)['data']
        return result
 
    def put(self, id):
        order = Order.query.get_or_404(id)
        orderDict = request.get_json(force=True)
        try:
            schema.validate(orderDict)
            requestDict = orderDict['data']['attributes']
            for key, value in requestDict.items():
                setattr(order, key, value)
 
            order.update()
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
        order = Order.query.get_or_404(id)
        try:
            delete = order.delete(order)
            response = make_response()
            response.status_code = 204
            return response
 
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp

api.add_resource(CreateListOrder, '.json')
api.add_resource(GetUpdateDeleteOrder, '/<int:id>.json')
