from app.database import db, orm

 
class Building(db.Model):
    __tablename__ = 'buildings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable = False)
    address = db.Column(db.String(256),nullable = False)
    latitude = db.Column(db.String(100),nullable = True)
    longitude = db.Column(db.String(100),nullable = True)
    category = db.Column(db.String(100), nullable = False)
    shelves = db.relationship('Shelf', backref='building', lazy=True, cascade="all, delete-orphan", passive_deletes=True)

    def __init__(self,  name,  address, latitude,  longitude, category, shelfId):
        self.name = name
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.category = category
        self.shelfId = shelfId

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()
 
    def update(self):
        return db.session.commit()
 
    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()