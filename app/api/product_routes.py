from flask import Blueprint, jsonify, session, request
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

@product_routes.route('/cart', methods=['POST'])
def get_cart_products():
    data = request.json
    product_ids_cart = data['productsArr']
    product_instance_list = []
    for product_id in product_ids_cart:
        product_instance_list.append(db.session.query(Product).filter(Product.id == product_id).first())
    return { "matchingProducts": [product.to_dict() for product in product_instance_list]}
