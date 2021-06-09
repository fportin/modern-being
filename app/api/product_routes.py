from flask import Blueprint, jsonify, session
from app.models import db, Product, Category

product_routes = Blueprint('product', __name__)

@product_routes.route('/categories/<int:categoryId>')
def get_products(categoryId):
    products = db.session.query(Product).join(Product.categories).filter(Category.id == categoryId).all()
    product_list = { "matchingProducts": [product.to_dict() for product in products]}
    # print(product_list)
    return product_list

@product_routes.route('/<int:productId>')
def get_product(productId):
    product = db.session.query(Product).filter(Product.id == productId).first()
    return product.to_dict()
