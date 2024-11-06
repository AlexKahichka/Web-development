# from pydantic import BaseModel, EmailStr, HttpUrl
#
#
# class Us_Adress(BaseModel):
#     city: str
#     street: str
#     house_number: int
#
#
# class User(BaseModel):
#     name: str
#     age: int
#     email: EmailStr
#     address: Us_Adress
#
#
# request_data =  """{
# "name": "John Doe",
# "age": 22,
# "email": "john.doe@example.com",
# "address": {
# "city": "New York",
# "street": "5th Avenue",
# "house_number": 123
# }
# }"""
#
#
# user1 = User.model_validate_json(request_data)
# print(user1.model_dump_json())
from pydantic import BaseModel, EmailStr


class User_Address(BaseModel):
    city: str
    street: str
    house_number: int


class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    address: User_Address


request_data = """"{
'name': 'Jon',
'age': 50,
'email': 'someemai@mail.de,
'city':
'address': 'some_Address',
'street': 'some street'
'house_number': 123
}
}
"""

user1 = User.parse_raw(request_data)
print(user1.model_dump_json())
