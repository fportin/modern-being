from flask import Blueprint, jsonify, session, request
from sqlalchemy import func
from app.models import db, Product, Category, Review

product_routes = Blueprint('product', __name__)

@product_routes.route('/categories/<int:categoryId>')
def get_products(categoryId):
    # products = db.session.query(Product, Review).join(Product.categories, Review).filter(
    #     Category.id == categoryId and Product.id == Review.productId).order_by(Product.id.asc()).all()
    # print(products)
    products = db.session.query(Product).join(Product.categories).filter(Category.id == categoryId).all()
    product_reviews = [(product, db.session.query(Review).filter(product.id == Review.productId).all()) for product in products]
    products_with_ratings = [(product.to_dict(), round(sum([review.rating for review in reviews])/len(reviews), 1), len(reviews)) for (product, reviews) in product_reviews]
    product_list = []
    for (product, rating, reviewers) in products_with_ratings:
        current_product = product
        current_product['rating'] = rating
        current_product['reviewers'] = reviewers
        product_list.append(current_product)
    complete_list = { "matchingProducts": product_list}
    # print(complete_list)
    return complete_list

@product_routes.route('/<int:productId>')
def get_product(productId):
    product = db.session.query(Product).filter(Product.id == productId).first()
    product_reviews = db.session.query(Review).filter(product.id == Review.productId).all()
    product_rating = round(sum([review.rating for review in product_reviews])/len(product_reviews), 1)
    current_product = product.to_dict()
    current_product['rating'] = product_rating
    current_product['reviewers'] = len(product_reviews)
    return current_product

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
    products = db.session.query(Product).join(Product.categories).filter(
        func.concat(' ', Category.type, ' ').ilike(f'% {term} %') |
        func.concat(' ', Product.brand, ' ').ilike(f'% {term} %') |
        func.concat(' ', Product.name, ' ').ilike(f'% {term} %')
    ).all()
    if not products:
        products = db.session.query(Product).filter(
            func.concat(' ', Product.description, ' ').ilike(f'% {term} %')
        ).all()
    product_reviews = [(product, db.session.query(Review).filter(product.id == Review.productId).all()) for product in products]
    products_with_ratings = [(product.to_dict(), round(sum([review.rating for review in reviews])/len(reviews), 1), len(reviews)) for (product, reviews) in product_reviews]
    product_list = []
    for (product, rating, reviewers) in products_with_ratings:
        current_product = product
        current_product['rating'] = rating
        current_product['reviewers'] = reviewers
        product_list.append(current_product)
    complete_list = {"matchingProducts": product_list}
    # print(complete_list)
    return complete_list
