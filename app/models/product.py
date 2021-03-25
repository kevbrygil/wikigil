from app.database import db
 
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable = False)
    sku = db.Column(db.String(100), unique=True, nullable = False)
    price = db.Column(db.Float, nullable = False)
    size = db.Column(db.String(100), nullable = False)
 
    def __init__(self, name, sku, price, size):
        self.name = name
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