from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator


class Address(BaseModel):
    city: str = Field(..., min_length=2)
    street: str = Field(..., min_length=3)
    house_number: int = Field(..., ge=0)

class User(BaseModel):
    name: str = Field(..., min_length=2)
    age: int = Field(..., gt=0, lt=120)
    email: EmailStr
    is_employed: bool
    address: Address

    @field_validator("name")
    def validate_name(cls, value: str) -> str:
        if not value.isalpha():
            raise ValueError("Name can contain only letters.")
        return value

    @model_validator(mode="after")
    def validate_employment_age(self) -> "User":
        if self.age < 18 and self.is_employed:
            raise ValueError("Employment age cannot be less than 18 years.")
        return self

def validate_json_string(json_string: str) -> str:
    user = User.model_validate_json(json_string)
    return user.model_dump_json()

# Sample JSON strings
valid_json = """
{ "name": "Alex",
    "age": 20,
    "email": "alex.martin@mail.com",
    "is_employed": true,
    "address": {
        "city": "Berlin",
        "street": "Hauptstr.",
        "house_number": 5
    }
}
"""

invalid_json = """
{ "name": "A1ex",
    "age": 15,
    "email": "alex.martin@mail.com",
    "is_employed": true,
    "address": {
        "city": "Berlin",
        "street": "Hauptstr.",
        "house_number": 5
    }
}
"""

# Example of correct data
valid_user = validate_json_string(valid_json)
print(valid_user)

print("*" * 100)

# Example of incorrect data
try:
    invalid_user = validate_json_string(invalid_json)
    print(invalid_user)
except ValueError as e:
    print("Validation error:", e)
