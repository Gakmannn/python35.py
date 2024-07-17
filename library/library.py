from __future__ import annotations
import statemanager as sm
import uuid
import datetime

class Human:
  def __init__ (self, name:str, snils:int, year:int):
    self.snils = snils
    self.name = name
    self.year = year
  def __repr__(self) -> str:
    return f'{self.snils} {self.name} {self.year}'

class Librarian(Human):
  pass

class Reader(Human):
  pass  
      
class Book:
  def __init__ (self, author:str, title:str, year:int, taked=False,card=None):
    self.author = author
    self.title = title
    self.year = year
    self.taked = taked
    self.idbn = uuid.uuid4()
    self.card = card if card else []
  def take(self, reader:Reader, librarian:Librarian):
    self.taked = True
    self.card.append({
      'reader': reader, 
      'librarian': librarian, 
      'returnBefore':datetime.datetime.now() + datetime.timedelta(days=7), 
      'returned': None
    })
    # Library.save(self)
  def getBack(self):
    self.taked = False
    self.card[-1]['returned'] = datetime.datetime.now()
    # Library.save(self)
    

class Library:
  def __init__(self): 
    self.data = {'books': [],'librarians': [],'readers': [],}
    sm.load(self.data)
    
  def save(self, el:Book|Human):
    sm.save(el, self.data)

  def add(self, el:Book|Human):
    name = el.__class__.__name__.lower()
    self._data[name+'s'].append(el)
    self.save(el)
    
  def remove(self, el:Book|Human):
    name = el.__class__.__name__.lower()
    self._data[name+'s'].remove(el)
    self.save(el)