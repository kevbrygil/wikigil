#Mapear las clases para los endpoints de la API
from flask import Blueprint
from flask_restful import Api
from app.controllers.order import ListOrders, CreateOrder, \
                                GetOrderById, UpdateOrderById, DeleteOrderById

order = Blueprint('order', __name__)
api = Api(order)

api.add_resource(ListOrders, '.json')
api.add_resource(CreateOrder, '.json')
api.add_resource(GetOrderById, '/<int:id>.json')
api.add_resource(UpdateOrderById, '/<int:id>.json')
api.add_resource(DeleteOrderById, '/<int:id>.json')