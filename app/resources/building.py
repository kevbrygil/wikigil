#Mapear las clases para los endpoints de la API
from flask import Blueprint
from flask_restful import Api
from app.controllers.building import ListCategories,ListBuildings, CreateBuilding, \
                                GetBuildingById, UpdateBuildingById, DeleteBuildingById

building = Blueprint('building', __name__)
api = Api(building)

api.add_resource(ListBuildings, '.json')
api.add_resource(CreateBuilding, '.json')
api.add_resource(ListCategories, '/categories.json')
api.add_resource(GetBuildingById, '/<int:id>.json')
api.add_resource(UpdateBuildingById, '/<int:id>.json')
api.add_resource(DeleteBuildingById, '/<int:id>.json')