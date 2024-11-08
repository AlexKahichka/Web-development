Task 1: Create an engine instance to connect to an in-memory SQLite database.

Task 2: Create a session to interact with the database using the created engine.

Task 3: Define a model for a product, Product, with the following column types:

id: numeric identifier
name: string (max. 100 characters)
price: numeric value with fixed precision
in_stock: boolean value.
Task 4: Define an associated model for a category, Category, with the following column types:

id: numeric identifier
name: string (max. 100 characters)
description: string (max. 255 characters)
Task 5: Establish a relationship between the Product and Category tables using the category_id column.