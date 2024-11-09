from hw4 import engine
from hw4.connector import DBConnector
from hw4.models import Category, Product

def add_test_data():
    with DBConnector(engine) as session:
        categories = [
            Category(
                name="Electronics",
                description="Gadgets and devices."
            ),
            Category(
                name="Books",
                description="Printed and e-books."
            ),
            Category(
                name="Clothing",
                description="Clothes for men and women."
            )
        ]
        session.add_all(categories)
        session.commit()

        products = [
            Product(
                name="Smartphone",
                price=299.99,
                in_stock=True,
                category_id=1
            ),
            Product(
                name="Laptop",
                price=499.99,
                in_stock=True,
                category_id=1
            ),
            Product(
                name="Science Fiction Novel",
                price=15.99,
                in_stock=True,
                category_id=2
            ),
            Product(
                name="Jeans",
                price=40.50,
                in_stock=True,
                category_id=3
            ),
            Product(
                name="T-shirt",
                price=20.00,
                in_stock=True,
                category_id=3
            )
        ]
        session.add_all(products)
        session.commit()
