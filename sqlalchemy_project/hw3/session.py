import logging

from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from sqlalchemy_project import engine
from sqlalchemy_project.hw3 import models
from sqlalchemy_project.hw3.models import Category, Product

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("sqlalchemy_project.engine")
logger.setLevel(logging.INFO)

models.main()

Session = sessionmaker(bind=engine)
session = Session()
session.execute(text("PRAGMA foreign_keys=ON"))

# Создаем категории
electronics_category = Category(
    name="Electronics",
    description="Electronic devices"
)

furniture_category = Category(
    name="Furniture",
    description="Household furniture"
)

session.add(electronics_category)
session.add(furniture_category)

# Создаем экземпляры продуктов
product_1 = Product(
    name="Smartphone",
    price=299.99,
    in_stock=True,
    category_id=1
)

product_2 = Product(
    name="Office Chair",
    price=89.99,
    in_stock=True,
    category_id=2
)

session.add(product_1)
session.add(product_2)
session.commit()


category = session.query(Category).filter(Category.id == 2).first()

session.delete(category)
session.commit()


products = session.query(Product).all()

for pr in products:
    print(f"prod_name={pr.name}")

session.close()
