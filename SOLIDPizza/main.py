from abc import ABC
from typing import List, Dict
from config import PAYMENT, TOPPING_PORTION

class Pizzeria:
  def __init__(self):
    self.data = {
      'menu': [],
      'cashRegister': [],
      'storage': [],
    }
  def addToMenu(self, pizza):
    pass
  def removeFromMenu(self, pizza):
    pass
  def addToStorage(self, topping):
    pass
  def takeToStorage(self, topping):
    pass
       

def save(el, data):
  name = el.__class__.__name__.lower()
  with open(name+'s.pickle', 'wb') as f:
    pickle.dump([], f)
  
  
class Topping:
  def __init__(self, name, costPrice, percent, count, portion):
    self.name = name
    self.costPrice = costPrice
    self.percent = percent
    self.count = count
    self.portion = portion
  def add(self):
    self.count -= self.portion
    return self.name    
    
#  'Onion': 0.015,
#   'Halapenio': 0.020,
#   'Chili': 0.010,
#   'Pickles': 0.015,
#   'Olives': 0.02,
#   'Prosuto': 0.02 
  
class Onion(Toppings):
  pass 
  
  
class Pizza:
  def __init__(self) -> None:
    self.toppings = []
    
class Console:
  pass


