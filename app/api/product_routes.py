from flask import Blueprint, jsonify, session
from app.models import db, Product

product_routes = Blueprint('product', __name__)

@product_routes.route('/')
def get_products():
    products = db.session.query(Product).all()
    product_list = { "products": [product.to_dict() for product in products]}
    print(product_list)
    return product_list
