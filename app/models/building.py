from app.database import db
from enum import IntEnum

class BuildingCategory(IntEnum):
    WAREHOUSE = 1
    CHAIN = 2
    SUPERMARKET = 3
    HYPERMARKET = 4
 
class Building(db.Model):
    __tablename__ = 'buildings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable = False)
    address = db.Column(db.String(256),nullable = False)
    latitude = db.Column(db.String(100),nullable = True)
    longitude = db.Column(db.String(100),nullable = True)
    category = db.Column(db.Enum(BuildingCategory), nullable = False)
    shelves = db.relationship('Shelf', back_populates='building', lazy=True, cascade="all, delete-orphan", passive_deletes=True)
    orders = db.relationship('Order', back_populates='building', lazy=True, cascade="all, delete-orphan", passive_deletes=True)

    def __init__(self,  name,  address, latitude,  longitude, category):
        self.name = name
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.category = category

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()
 
    def update(self):
        return db.session.commit()
 
    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()