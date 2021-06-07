from app.models import db, Product, Category

# sets relationship between product and category, you can add product and its categories here if you want
def seed_product_categories():

    for product_id in range(1,13):
        product = Product.query.get(product_id)
        category1 = Category.query.get(1)
        category2 = Category.query.get(11)
        product.categories.append(category1)
        product.categories.append(category2)

    for product_id in range(13,23):
        product = Product.query.get(product_id)
        category1 = Category.query.get(2)
        category2 = Category.query.get(11)
        product.categories.append(category1)
        product.categories.append(category2)

    for product_id in range(23,33):
        product = Product.query.get(product_id)
        category1 = Category.query.get(3)
        category2 = Category.query.get(11)
        product.categories.append(category1)
        product.categories.append(category2)
    
    for product_id in range(33,43):
        product = Product.query.get(product_id)
        category1 = Category.query.get(4)
        category2 = Category.query.get(14)
        product.categories.append(category1)
        product.categories.append(category2)

    for product_id in range(43,53):
        product = Product.query.get(product_id)
        category1 = Category.query.get(5)
        category2 = Category.query.get(14)
        product.categories.append(category1)
        product.categories.append(category2)

    for product_id in range(53,63):
        product = Product.query.get(product_id)
        category1 = Category.query.get(6)
        category2 = Category.query.get(13)
        product.categories.append(category1)
        product.categories.append(category2)

    for product_id in range(63,73):
        product = Product.query.get(product_id)
        category1 = Category.query.get(7)
        category2 = Category.query.get(12)
        product.categories.append(category1)
        product.categories.append(category2)

    for product_id in range(73,83):
        product = Product.query.get(product_id)
        category1 = Category.query.get(8)
        category2 = Category.query.get(12)
        product.categories.append(category1)
        product.categories.append(category2)

    for product_id in range(83,93):
        product = Product.query.get(product_id)
        category1 = Category.query.get(9)
        category2 = Category.query.get(13)
        product.categories.append(category1)
        product.categories.append(category2)

    for product_id in range(93,103):
        product = Product.query.get(product_id)
        category1 = Category.query.get(10)
        category2 = Category.query.get(13)
        product.categories.append(category1)
        product.categories.append(category2)

    db.session.commit()
