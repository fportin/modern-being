from flask import Blueprint, jsonify, session
from app.models import db, Category, Product
from  sqlalchemy.sql.expression import func

category_routes = Blueprint('category', __name__)

@category_routes.route('/')
def get_categories():
    categories = db.session.query(Category).all()
    results = []
    for category in categories:
        sample_product = db.session.query(Category, Product).join(Category.products).filter(Category.id == category.id).order_by(func.random()).first()
        results.append(sample_product)
    category_list = { "matchingCategories": [(category[0].to_dict(), category[1].to_dict()) for category in results]}
    # print(category_list)
    return category_list
