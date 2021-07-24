from app.database import db
 
class Shelf(db.Model):
    __tablename__ = 'shelves'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable = False)
    maxCapacity = db.Column(db.Integer,nullable = False)
    itemsAvailables = db.Column(db.Integer,nullable = False)
    latitude = db.Column(db.String(100),nullable = True)
    longitude = db.Column(db.String(100),nullable = True)
    personId = db.Column(db.Integer, db.ForeignKey('persons.id'), ondelete = 'CASCADE')
    buildingId = db.Column(db.Integer, db.ForeignKey('buildings.id'), ondelete = 'CASCADE')
    building = db.relationship('Building', back_populates = 'shelves')
 
    def __init__(self,  name,  maxCapacity, latitude,  longitude, buildingID):
        self.name = name
        self.maxCapacity = maxCapacity
        self.latitude = latitude
        self.longitude = longitude
        self.buildingID = buildingID
         
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()
 
    def update(self):
        return db.session.commit()
 
    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()