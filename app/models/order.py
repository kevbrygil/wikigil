import datetime
from app.database import db
 
class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150),nullable = False)
    stockCount = db.Column(db.Integer, nullable = False)
    orderDate = db.Column(db.DateTime, default = datetime.datetime.now)

    buildingId = db.Column(db.Integer, db.ForeignKey('buildings.id'), nullable = False)
    building = db.relationship('Building', back_populates = 'orders')

    productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable = False)
    product =db.relationship('Product', back_populates = 'orders')

    employeeId = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable = False)
    employee =db.relationship('Employee', back_populates = 'orders')
 
    def __init__(self,  name,  stockCount, buildingId, productId, employeeId):
        self.name = name.lower()
        self.stockCount = stockCount
        self.buildingId = buildingId
        self.productId = productId
        self.employeeId = employeeId
         
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()
 
    def update(self):
        return db.session.commit()
 
    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()