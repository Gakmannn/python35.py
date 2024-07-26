from library import Library, Book, Human, Librarian, Reader
from app import App, ScreenLogger, FileLogger
import sys

class Menu:
  def login(self, uuid):
    pass

class UserMenu(Menu):
  def __init__(self):
    self.user = None
    self.dict = {
      '1': {'text':'Взять книгу', 'func':self.take},
      '2': {'text':'Вернуть книгу', 'func':self.back},
      '3': {'text':'Аннулировать читательский', 'func':self.remove},
      '4': {'text':'Выйти', 'func':self.exit},
    }
    self.login()
  def login(self):
    while not self.user:
      code = input('Введите номер читательского билета')
      if code == 'exit':
        exit()
      try:
        snils = int(code)
        self.user = app.find(interf[appType], snils)
        print (f'Привет, {self.user.name}')
        while (self.user):
          print ('Выберите действие:')
          for key in self.dict:
            print(key+'. '+self.dict[key]['text'])
          a = input()
          self.dict[a]['func']()
      except:
        print('Проверьте правильность ввода')  
  def take(self):
    pass
  def back(self):
    pass
  def remove(self):
    pass
  def exit(self):
    self.user = None

class LibMenu(Menu):
  pass      
class BoosMenu(Menu):
  pass      
  
def hello():
  print ('Укажите дополнительный параметр для работы в определённом окружении:')
  print ('1. Окружение читателя')
  print ('2. Окружение библиотекаря')
  print ('3. Окружение руководителя')

interf = {
  "1": "readers",
  "2": "librarians"
}

if __name__ == "__main__":
  try:
    sys.argv[1]
  except:
    hello()
    exit()
  
  app = App()
  app = FileLogger(app)
  try:
    if sys.argv[2]=='1':
      app = ScreenLogger(app)
  except:
    pass

  user = None
  appType = sys.argv[1]
  if appType == '1':
    UserMenu()   
  if appType == '2':
    LibMenu()   
  if appType == '3':
    BoosMenu()
  else:
    print ('Неверно введён дополнительный параметр.')
    hello()