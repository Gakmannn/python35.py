from library import Library

class app:
  library:Library
  @staticmethod
  def init():
    app.library = Library()
    print(app.library.__dict__)
  @staticmethod
  def add(usr:int, ):
    pass
  @staticmethod
  def remove():
    pass
  @staticmethod
  def find(type, code):
    for el in app.library.data[type]:
      if el.snils==code:
        return el
    return None