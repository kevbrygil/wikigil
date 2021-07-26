from app.database import db
 
class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable = False)
    shelves = db.relationship('Shelf', back_populates='employee', lazy=True)
    orders = db.relationship('Order', back_populates='employee', lazy=True)

    def __init__(self,  name):
        self.name = name
        
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()
 
    def update(self):
        return db.session.commit()
 
    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()