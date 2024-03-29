from .db import db
from .productCategory import product_category

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    brand = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    photo = db.Column(db.String, nullable=False)

    categories = db.relationship(
        "Category", secondary=product_category, back_populates="products"
    )


    def to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "description": self.description,
        "brand": self.brand,
        "price": self.price,
        "photo": self.photo
        }