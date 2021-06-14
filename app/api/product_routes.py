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
    total = 0
    qty_total = 0
    for product_id, quantity in product_ids_cart.items():
        current_item = (db.session.query(Product).filter(Product.id == product_id).first()).to_dict()
        current_item['quantity'] = quantity
        current_item['subtotal'] = round(current_item['price'] * current_item['quantity'], 2)
        product_instance_list.append(current_item)
        total += current_item['subtotal']
        qty_total += current_item['quantity']
    return { "matchingProducts": product_instance_list, "total": total, "qty": qty_total }

@product_routes.route('/search', methods=['POST'])
def search_products():
    data = request.json
    term = data['searchTerm']
    products = db.session.query(Product).join(Product.categories).filter(Category.type.ilike(f'%{term}%') | Product.brand.ilike(f'%{term}%') | Product.name.ilike(f'%{term}%')).all()
    if not products:
        products = db.session.query(Product).filter(Product.description.ilike(f'%{term}%')).all()
    
    product_list = { "matchingProducts": [product.to_dict() for product in products]}
    return product_list