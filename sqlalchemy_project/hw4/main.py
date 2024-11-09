from sqlalchemy import func

from hw4 import engine, test_data, models
from hw4.connector import DBConnector
from hw4.models import Product, Category

CIAN = "\033[96m"
RESET = "\033[0m"

with DBConnector(engine) as session:
    models.create_entities()
    test_data.add_test_data()

    # Task 2: Data Retrieval. Retrieve all records from the categories table. For each category,
    # retrieve and display all associated products, including their names and prices.
    print(f"{CIAN}Task2{RESET}")
    categories: list[Category] = session.query(Category).all()

    for category in categories:
        products: list[Product] = session.query(Product).filter(Product.category_id == category.id).all()

        if products:
            print(f"Category: {category.name}")
            for product in products:
                print(f"{product.name:<30} | price: {product.price:<7} | in stock: {'Yes' if product.in_stock else 'No'}")
            print("*" * 100)

    # Task 3: Data Update. Find the first product with the name "Smartphone" in the products table.
    # Update its price to 349.99.
    print(f"{CIAN}Task3{RESET}")
    product: Product = session.query(Product).filter(Product.name == "Smartphone").one_or_none()
    if product:
        product.price = 349.99
        session.commit()

    new_product: Product = session.query(Product).filter(Product.name == "Smartphone").one_or_none()
    if new_product:
        print(f"{new_product.name} | {new_product.price}")
    print("*" * 100)

    # Task 4: Aggregation and Grouping
    # Using aggregate functions and grouping, count the total number of products
    # in each category.
    print(f"{CIAN}Task4{RESET}")
    products_in_category: list[Product] = session.query(Product, func.count(Product.id)
                                                        .label("amount_of_products")).group_by(Product.category_id)

    for product in products_in_category:
        print(f"Category: {product.Product.category.name:<13} | amount of products: {product.amount_of_products}")
    print("*" * 100)

    # Task 5: Grouping with Filtering
    # Filter and display only those categories that contain more than one product.
    print(f"{CIAN}Task5{RESET}")
    categories_more_one_item: list[Product] = session.query(
        Product
    ).group_by(Product.category_id).having(func.count(Product.id) > 1).all()

    if categories_more_one_item:
        for product in categories_more_one_item:
            print(f"Category name: {product.category.name}")
