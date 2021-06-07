from app.models import db, Category

# Adds a demo category, you can add other categories here if you want
def seed_categories():

    demo = [
        Category(type="Laptops"),
        Category(type="Desktops"),
        Category(type="Monitors"),
        Category(type="Headphones"),
        Category(type="Smart Speakers"),
        Category(type="Smart Watches"),
        Category(type="Smart Phones"),
        Category(type="Tablets"),
        Category(type="AR/VR Glasses"),
        Category(type="Gesture & Immersion"),
        Category(type="Computing"),
        Category(type="Mobile"),
        Category(type="Wearable"),
        Category(type="Audio")
        ]

    [db.session.add(item) for item in demo]

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_categories():
    db.session.execute('TRUNCATE categories RESTART IDENTITY CASCADE;')
    db.session.commit()
