from app.database import db
 
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150),nullable = False)
    stockCount = db.Column(db.Integer, nullable = False)
    storeid = db.Column(db.Integer, db.ForeignKey('store.id'))
    productid = db.Column(db.Integer, db.ForeignKey('product.id'))

    store = db.relationship('Store', foreign_keys=[storeid])
    product = db.relationship('Product', foreign_keys=[productid])
 
    def __init__(self,  name,  stockCount, storeid, productid):
        self.name = name.lower()
        self.stockCount = stockCount
        self.storeid = storeid
        self.productid = productid
         
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()
 
    def update(self):
        return db.session.commit()
 
    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()