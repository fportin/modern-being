from app.models import db, Review
from faker import Faker
import random


# Adds demo reviews, you can add other reviews here if you want
fake = Faker()
Faker.seed(0)

def seed_reviews():
    demo_body = [
        'Awesome product!', 
        'Good buy, very useful.', 
        'Very satisfied with my purchase',
        'Delivers what is promises.',
        'Definitely would recommend,',
        'Made the right choice.',
        'Very reliable.',
        'So happy with my purchase.',
        'Look no further, this is the product that you want',
        'Best choice to fulfill my need.' 
    ]
    
    for user in range(2, 102):
        for review in range(10):
            review = Review(
                            rating=random.randint(3,5),
                            body=random.choice(demo_body),
                            productId=random.randint(1,102),
                            userId=user
                        )
            db.session.add(review)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key


def undo_reviews():
    db.session.execute('TRUNCATE reviews RESTART IDENTITY CASCADE;')
    db.session.commit()
