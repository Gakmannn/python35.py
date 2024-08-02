from marshmallow import Schema, fields, validate, post_load
import json

class User:
  def __init__(self, email, books=[]):
    self.email = email
    self.books = books
  def __repr__(self) -> str:
    str =  f'{self.email} Books:\n'
    for book in self.books:
      str += f'\t{book}\n'
    return str

class Book:
  def __init__(self, title, isbn):
    self.title = title
    self.isbn = isbn
  def __repr__(self) -> str:
    return f'{self.title} {self.isbn}'

def validate_isbn(isbn: str) -> None:
    """ Код проверки isbn (опущено), бросает исключение 
    marshmallow.ValidationError если валидация не прошла"""

class BookSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(max=120))
    isbn = fields.String(required=True, validate=validate_isbn)
    @post_load
    def make_obj(self, data, **kwargs):
        print ('Создан объект Book с title ' + data['title'])
        return Book(**data)

class UserSchema(Schema):
    email = fields.Email(required=True)
    books = fields.Nested(BookSchema, many=True, required=False)
    @post_load
    def make_obj(self, data, **kwargs): # название метода может быть любым
        return User(**data)

raw_data_str = """{
    "email": "foo@bar.com",
    "books": [
        {"title": "Автостопом по Галактике", "isbn": "123456789"},
        {"title": "Идеальный программист", "isbn": "987654321"}
    ]
}"""
json_data = json.loads(raw_data_str)
schema = UserSchema()
user = schema.load(json_data) # бросает исключение если валидация не прощла


print(user)