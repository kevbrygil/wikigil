from flask import request, jsonify, make_response
from flask_restful import Resource
from app.database import db
from app.models.building import Building, BuildingCategory
from app.schemas.building import BuildingSchema
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError
import json

schema = BuildingSchema()

class ListCategories(Resource):
    def get(self):
        return json.dumps([(category.value, category.name) for category in BuildingCategory])

class ListBuildings(Resource):
    def get(self):
        building_query = Building.query.all()
        results = schema.dump(building_query, many=True)
        return results

class CreateBuilding(Resource):
    def post(self):
        requestBuilding = request.get_json(force=True)
        try:
            schema.validate(requestBuilding)
            request_dict = schema.load(requestBuilding)
            building = Building(request_dict['name'],
                                request_dict['address'],
                                request_dict['latitude'],
                                request_dict['longitude'],
                                request_dict['category'])
            building.add(building)
            query = Building.query.get(building.id)
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

class GetBuildingById(Resource):
    def get(self, id):
        building_query = Building.query.get_or_404(id)
        result = schema.dump(building_query)
        return result

class UpdateBuildingById(Resource):
    def put(self, id):
        building = Building.query.get_or_404(id)
        requestBuilding = request.get_json(force=True)
        try:
            schema.validate(requestBuilding)
            request_dict = schema.load(requestBuilding)
            for key, value in request_dict.items():
                setattr(Building, key, value)
 
            building.update()
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

class DeleteBuildingById(Resource):
    def delete(self, id):
        building = Building.query.get_or_404(id)
        try:
            building.delete(building)
            response = make_response()
            response.status_code = 204
            return response

        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp