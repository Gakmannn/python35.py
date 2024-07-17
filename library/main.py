from library import Library, Book, Human, Librarian, Reader
from app import app
import sys

class Menu:
  def login(self, uuid):
    pass

class userMenu(Menu):
  def __init__(self):
    self.user = None
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
          self.menu()
          a = input()
          if a == '1':
            pass
          if a == '2':
            pass
          if a == '3':
            pass
          if a == '4':
            self.user = None
      except:
        print('Проверьте правильность ввода')  
  def menu(self):
    print ('Выберите действие:')
    print ('1. Взять книгу')
    print ('2. Вернуть книгу')
    print ('3. Аннулировать читательский')
    print ('4. Выйти')
      
class libMenu(Menu):
  pass      
class boosMenu(Menu):
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
  
  app.init()
  
  user = None
  appType = sys.argv[1]
  if appType == '1':
    userMenu()   
  if appType == '2':
    libMenu()   
  if appType == '3':
    boosMenu()
  else:
    print ('Неверно введён дополнительный параметр.')
    hello()