from abc import ABC
from typing import List, Dict
from statemanager import load, save

class Pizzeria:
  def __init__(self):
    Pizza.load()
    Topping.load()
    self.data = {
      'menu': Pizza.data['pizzas'],
      'cashRegister': [],
      'toppings': Topping.data['toppings'],
    }
  def addToMenu(self, pizza):
    pass
  def removeFromMenu(self, pizza):
    pass
  def addToStorage(self, topping):
    pass
  def takeToStorage(self, topping):
    pass
  
class Money(ABC):
  def  __init__(self, count):
    self.count = count

class Fiat(Money):
  pass        
class Card(Money):
  pass        
  
class Topping:
  data = {
    'toppings': []
  }
  def __init__(self, name, costPrice, percent, count, portion):
    self.name = name
    self.costPrice = costPrice
    self.percent = percent
    self.count = count
    self.portion = portion
  def add(self):
    self.count -= self.portion
    return self.name   
  def __repr__(self):
    return f'{self.name} {self.count}' 
  @classmethod
  def find(cls, toppingName):
    for el in cls.data['toppings']:
      if el.name == toppingName:
        return el
    return None
  @classmethod
  def load(cls):
    try:
      load(cls.data)
    except:
      cls.data['toppings'].append(cls('Onion', 1, 50, 5, 0.015))
      cls.data['toppings'].append(cls('Halapenio', 3, 50, 5, 0.02))
      cls.data['toppings'].append(cls('Chili', 2, 50, 5, 0.010))
      cls.data['toppings'].append(cls('Pickles', 2, 50, 5, 0.015))
      cls.data['toppings'].append(cls('Olives', 3, 50, 5, 0.02))
      cls.data['toppings'].append(cls('Prosuto', 5, 50, 5, 0.02))
      cls.save()
  @classmethod
  def save(cls):
    save('Topping', cls.data) 
        
class Pizza:
  data = {
    'pizzas': []
  }
  def __init__(self, name, toppings=None) -> None:
    self.name = name 
    self.toppings = toppings if toppings else []
    self.calc()
  def add(self, toppingName):
    self.toppings.append(toppingName)
    return self
  def calc(self):
    costPrice = 1
    sum = 1.5 # Base price (work + dough)
    for toppingName in self.toppings:
      topping = Topping.find(toppingName)
      if topping:
        sum += topping.portion * topping.costPrice * (100 + topping.percent)/100
        costPrice += topping.portion * topping.costPrice
    self.price = round(sum, 1)
    self.costPrice = round(costPrice, 3)
  @classmethod
  def load(cls):
    try:
      load(cls.data)
    except:
      cls.data['pizzas'].append(cls('Beef', ['Prosuto','Prosuto','Prosuto','Olives','Pickles','Halapenio']))
      cls.data['pizzas'].append(cls('SelfMade'))
      cls.save()
  @classmethod
  def save(cls):
    save('Pizza', cls.data)
  
class Order:
  def __init__(self, pizzas=None):
    self.pizzas = pizzas if pizzas else []
    sum = 0
    cost = 0
    for pizza in self.pizzas:
      print(pizza.__dict__)
      sum += pizza.price
      cost += pizza.costPrice
    self.sum = sum
    self.cost = cost
    self.isPayd = False
    self.isBaked = False
  def bake(self):
    res = []
    if self.isPayd and not self.isBaked:
      for pizza in self.pizzas:
        for toppingName in pizza.toppings:
          topping = Topping.find(toppingName)
          if topping:
            topping.add()
        res.append(pizza.name + 'готова')
      self.isBaked = True
    return res
  def pay(self, money:Money):
    self.payment = money
    self.isPayd = True
    return self.bake()  
      
class Console:
  pass

# Pizza.load()
app = Pizzeria()
print (app.__dict__)
myOrder = Order([app.data['menu'][0]])
print(myOrder.pay(Card(myOrder.sum)))
print (app.__dict__)


def runApp():
  pass