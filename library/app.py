from library import Library

class App:
  def __init__(self):
    self.library = Library()
    print(self.library.__dict__)
  def add(self,usr:int, ):
    pass
  def remove(self,):
    pass
  def find(self,type, code):
    for el in self.library.data[type]:
      if el.snils==code:
        return el
    return None
  
class ScreenLogger:
  def __init__(self, app):
    self.app = app
  def add(self,usr:int, ):
    self.app.add(usr)
    pass
  def remove(self,):
    self.app.remove(usr)
    pass
  def find(self,type, code):
    res = self.app.find(type, code)
    return res

class FileLogger:
  def __init__(self, app):
    self.app = app
  def add(self,usr:int, ):
    self.app.add(usr)
    pass
  def remove(self,):
    self.app.remove(usr)
    pass
  def find(self,type, code):
    res = self.app.find(type, code)
    return res
