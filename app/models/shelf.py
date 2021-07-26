from app.models.employee import Employee
from app.database import db
 
class Shelf(db.Model):
    __tablename__ = 'shelves'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable = False)
    maxCapacity = db.Column(db.Integer,nullable = False)
    availablesItems = db.Column(db.Integer,nullable = False)
    latitude = db.Column(db.String(100),nullable = True)
    longitude = db.Column(db.String(100),nullable = True)

    employeeId = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable = False)
    employee =db.relationship('Employee', back_populates = 'shelves')

    productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable = False)
    product =db.relationship('Product', back_populates = 'shelves')

    buildingId = db.Column(db.Integer, db.ForeignKey('buildings.id'), nullable = False)
    building = db.relationship('Building', back_populates = 'shelves')

    def __init__(self,  name,  maxCapacity, availablesItems, latitude,  longitude, employeeId, productId, buildingId):
        self.name = name
        self.maxCapacity = maxCapacity
        self.availablesItems = availablesItems
        self.latitude = latitude
        self.longitude = longitude
        self.employeeId = employeeId
        self.productId = productId
        self.buildingId = buildingId

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()
 
    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()