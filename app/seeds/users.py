from werkzeug.security import generate_password_hash
from app.models import db, User
from faker import Faker


# Adds a demo user, you can add other users here if you want
fake = Faker()
Faker.seed(0)
def seed_users():

    demo = User(username='Demo', email='demo@aa.io',
                password='password')

    db.session.add(demo)

    for user in range(100):
        user = User(
                    username=fake.name(),
                    email=fake.email(), 
                    password='fake-user-password'
                    )
        db.session.add(user)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
