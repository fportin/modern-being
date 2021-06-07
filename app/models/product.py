from .db import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String, nullable=False)


    def to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "description": self.description,
        "brand": self.brand,
        "price": self.price,
        "photo": self.photo
        }