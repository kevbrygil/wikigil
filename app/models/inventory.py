from app.database import db
 
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150),nullable = False)
    stock = db.Column(db.Integer, nullable = False)
    shelfcount = db.Column(db.Integer, nullable = False)
    storeid = db.Column(db.Integer, db.ForeignKey('store.id'))
    productid = db.Column(db.Integer, db.ForeignKey('product.id'))
    shelfid = db.Column(db.Integer, db.ForeignKey('shelf.id'))

    store = db.relationship('Store', foreign_keys=[storeid])
    product = db.relationship('Product', foreign_keys=[productid])
    shelf = db.relationship('Shelf', foreign_keys=[shelfid])
 
    def __init__(self,  name,  stock, shelfcount, storeid, productid, shelfid):
        self.name = name.lower()
        self.stock = stock
        self.shelfcount = shelfcount
        self.storeid = storeid
        self.productid = productid
        self.shelfid = shelfid
         
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()
 
    def update(self):
        return db.session.commit()
 
    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()