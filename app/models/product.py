from app.database import db
 
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(100), unique=True, nullable = False)
    price = db.Column(db.DECIMAL(10,2), nullable = False)
    size = db.Column(db.String(100), nullable = False)
 
    def __init__(self, sku, price, size):
        self.sku = sku
        self.price = price
        self.size = size
         
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()
 
    def update(self):
        return db.session.commit()
 
    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()