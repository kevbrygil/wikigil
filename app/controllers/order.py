from flask import request, jsonify, make_response
from flask_restful import Resource
from app.database import db
from app.models.order import Order
from app.schemas.order import OrderSchema
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError
 
schema = OrderSchema()

class ListOrders(Resource):
    def get(self):
        orderQuery = Order.query.all()
        results = schema.dump(orderQuery, many=True)
        return results

class CreateOrder(Resource):
    def post(self):
        requestOrder = request.get_json(force=True)
        try:
            schema.validate(requestOrder)
            orderDict = schema.load(requestOrder)
            order = Order(orderDict['name'],
                        orderDict['stockCount'],
                        orderDict['buildingId'],
                        orderDict['productId'],
                        orderDict['employeeId'])
            order.add(order)
            results = schema.dump(order)
            query = Order.query.get(order.id)
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

class GetOrderById(Resource):
    def get(self, id):
        orderQuery = Order.query.get_or_404(id)
        result = schema.dump(orderQuery)
        return result

class UpdateOrderById(Resource):
    def put(self, id):
        order = Order.query.get_or_404(id)
        requestOrder = request.get_json(force=True)
        try:
            schema.validate(requestOrder)            
            orderDict = schema.load(requestOrder)
            for key, value in orderDict.items():
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

class DeleteOrderById(Resource):
    def delete(self, id):
        order = Order.query.get_or_404(id)
        try:
            order.delete(order)
            response = make_response()
            response.status_code = 204
            return response
 
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp