#Mapear las clases para los endpoints de la API
from flask import Blueprint
from flask_restful import Api
from app.controllers.product import ListProducts, CreateProduct, \
                                GetProductById, UpdateProductById, DeleteProductById

product = Blueprint('product', __name__)
api = Api(product)

api.add_resource(ListProducts, '.json')
api.add_resource(CreateProduct, '.json')
api.add_resource(GetProductById, '/<int:id>.json')
api.add_resource(UpdateProductById, '/<int:id>.json')
api.add_resource(DeleteProductById, '/<int:id>.json')