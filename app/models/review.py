from .db import db

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, db.CheckConstraint('rating > 0 and rating <= 5'), nullable=False)
    body = db.Column(db.Text, nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey('products.id'))
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))


    def to_dict(self):
        return {
        "id": self.id,
        "rating": self.rating,
        "body": self.body,
        "productId": self.productId,
        "userId": self.userId
        }