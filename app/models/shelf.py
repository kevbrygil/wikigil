from app.database import db
 
class Shelf(db.Model):
    __tablename__ = 'shelves'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable = False)
    capacity = db.Column(db.Integer,nullable = False)
    latitude = db.Column(db.String(100),nullable = True)
    longitude = db.Column(db.String(100),nullable = True)

    storeid = db.Column(db.Integer, db.ForeignKey('store.id'))
    store = db.relationship('Store', foreign_keys=[storeid])
    building = db.relationship('Building', back_populates = 'shelves')
 
    def __init__(self,  name,  capacity, latitude,  longitude, storeid):
        self.name = name
        self.capacity = capacity
        self.latitude = latitude
        self.longitude = longitude
        self.storeid = storeid
         
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()
 
    def update(self):
        return db.session.commit()
 
    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()