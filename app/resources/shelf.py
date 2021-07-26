#Mapear las clases para los endpoints de la API
from flask import Blueprint
from flask_restful import Api
from app.controllers.shelf import ListShelves, CreateShelf, \
                                GetShelfById, UpdateShelfById, DeleteShelfById

shelf = Blueprint('shelf', __name__)
api = Api(shelf)

api.add_resource(ListShelves, '.json')
api.add_resource(CreateShelf, '.json')
api.add_resource(GetShelfById, '/<int:id>.json')
api.add_resource(UpdateShelfById, '/<int:id>.json')
api.add_resource(DeleteShelfById, '/<int:id>.json')