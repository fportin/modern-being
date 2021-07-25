from flask import Blueprint, session, request
from flask_login import current_user, login_required
from app.forms import ReviewForm
from app.models import db, Review, User
from .auth_routes import validation_errors_to_error_messages

review_routes = Blueprint('review', __name__)


@review_routes.route('/create', methods=['POST'])
@login_required
def create_review():
    """
    Creates a review.
    """
    form = ReviewForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if current_user.is_authenticated and form.validate_on_submit() and (current_user.id == form.data['userId']):
        review = Review(
            rating = form.data['rating'],
            body = form.data['body'],
            productId = form.data['productId'],
            userId = form.data['userId']
        )
        db.session.add(review)
        db.session.commit()
        return review.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@review_routes.route('/<int:productId>')
def get_reviews(productId):
    reviews = db.session.query(Review, User).join(User).filter(Review.productId == productId).order_by(Review.id.desc()).all()
    print(reviews)
    review_list = { "matchingReviews": [(review.to_dict(), user.to_dict()) for review, user in reviews]}
    return review_list

@review_routes.route('/<int:productId>/edit', methods=['PUT'])
@login_required
def edit_review(productId):
    target = request.json['target']
    review = db.session.query(Review).get(target)
    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if current_user.is_authenticated and form.validate_on_submit() and (current_user.id == form.data['userId']) and (productId == form.data['productId']) and (review.userId == current_user.id):
        review.rating = form.data['rating']
        review.body = form.data['body']
        db.session.commit()
        return review.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401     

@review_routes.route('/<int:productId>/delete', methods=['DELETE'])
@login_required
def delete_review(productId):
    target = request.json['target']
    userId = request.json['userId']
    prodId = request.json['productId']
    review = db.session.query(Review).get(target)
    if current_user.is_authenticated and (current_user.id == userId) and (productId == prodId) and (review.userId == current_user.id):
        db.session.delete(review)
        db.session.commit()
        return { "message": 'The Review has been deleted.' }   
    return {'errors': 'There was an error in validating the delete request.'}, 401    
