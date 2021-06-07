from .db import db
from .productCategory import product_category

class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String, nullable=False)

    products = db.relationship(
        "Product", secondary=product_category, back_populates="categories"
    )