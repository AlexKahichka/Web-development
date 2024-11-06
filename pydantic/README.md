# Pydantic (Pydantic)
# This folder contains assignments for Pydantic. (Dieser Ordner enthält Aufgaben für Pydantic.)
# Task 1:
Develop a user registration system using Pydantic for input validation, handling of nested structures, and serialization. The system should process data in JSON format.

Tasks:
Create data model classes using Pydantic for the user and their address.
Implement a function that takes a JSON string, deserializes it into Pydantic objects, validates the data, and if successful, serializes the object back to JSON and returns it.
Add a custom validator to check the consistency of the user's age and employment status.
Write several JSON string examples to test various validation scenarios: successful registrations and cases where validation fails (e.g., age does not match employment status).
Models:
Address: Should contain the following fields:

city: string, minimum of 2 characters.
street: string, minimum of 3 characters.
house_number: number, must be positive.
User: Should contain the following fields:

name: string, must be alphabetic characters only, minimum of 2 characters.
age: number, must be between 0 and 120.
email: string, must follow email format.
is_employed: boolean, user's employment status.
address: nested address model.
