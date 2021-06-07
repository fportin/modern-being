from .db import db

product_category = db.Table(
    "product_categories",
    db.Column("productId", db.Integer, db.ForeignKey("products.id"), primary_key=True),
    db.Column("categoryId", db.Integer, db.ForeignKey("categories.id"), primary_key=True)
)