from __future__ import annotations
import contextlib
import string
import random
import pickle
# import statemanager as sm
import operator
import re
import time
import math as m
from math import pi as PI, sin as SinusFunction
from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator
from random import randrange
from typing import List, Any
import uuid
import inspect

with contextlib.suppress(ImportError):
    from pyscript import window
    input = window.prompt
    print = window.alert

def main():
  print("Let's compute π:")
  def compute_pi(n):
    pi = 2
    for i in range(1,n):
      pi *= 4 * i ** 2 / (4 * i ** 2 - 1)
    return pi

  pi = compute_pi(100000)
  s = f"π is approximately {pi:.3f}"
  print(s)

main()

print('Hello world', 'sfgdfg\\\'df', 15, sep="\n")
print(0o123)
print(0x53)
print(4==4.)

# Соглашение о именовании констант
DAY_IN_WEEK = 7
print(DAY_IN_WEEK)

a = None
A = 1

print(a, A)
a = 2
print(a)


# Запомните! На основе этого результата можно
# сформулировать следующие правила:
# ■ если аргументы по обе стороны от ** целые числа,
# результат тоже будет целым числом;
# ■ если хотя бы один аргумент ** будет числом с плавающей точкой, результат тоже будет числом
# с плавающей точкой.

print (2e2)
print (2. ** 2)
print (4 ** 0.5)

# int - целое чиcло
# float - чиcло с плавающей точкой

# Деление (результат int только, если оба int)
print(6 * 3) 
# Деление (результат float)
print(6 / 3) 
# Целочисленное деление (откидывает остаток)
print(6 // 3) 
print(7 // 3) 

#! Примечание: некоторые значения являются отрицательными. 
#! Очевидно, это повлияет на результат. Но как?
#! Результат — две отрицательные двойки. Реальный
#! (не округленный) результат -1.5 в обоих случаях. Тем не
#! менее, результаты всегда округляются. Округление идет
#! к меньшему целому значению, а меньшее целочисленное
#! значение — это -2, отсюда: -2 и -2.0.

print(-6 // 4)
print(6. // -4)

# !Операторы: как не делить
# Как вы, наверное, знаете, деление на ноль не работает.
# Не пытайтесь делать следующее:
# ■ делить на ноль;
# ■ делить целое число на ноль;
# ■ находить остаток от деления на ноль.

# Левостороннее связваение
print(9 % 6 % 2)
# Правостороннее связваение
print((2 ** 2) ** 3)


# Примечание. PEP 8 — руководство по коду на Python
# рекомендует следующее соглашение об именовании
# переменных и функций в Python:
# ■ Имена функций должны состоять из маленьких
# букв, а слова разделяться символами подчеркивания — это необходимо, чтобы их было легче
# прочитать (например, var, my_variable).
# ■ Имена функций соблюдают те же правила, что
# и имена переменных (например, fun, my_function).
# ■ Стиль mixedCase (смешанный регистр, например, myVariable) допускается в тех местах, где
# уже преобладает такой стиль, для сохранения
# обратной совместимости.

print(len(['False', 'None', 'True', 'and', 'as', 'assert',
'break', 'class', 'continue', 'def', 'del', 'elif',
'else', 'except', 'finally', 'for', 'from', 'global',
'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
'not', 'or', 'pass', 'raise', 'return', 'try',
'while', 'with', 'yield']))

print("Python version: " + str(3))
print(15 + int('3'))
print(15 + float('3'))
print(15 + bool('3'))
print(15 + bool(''))
print(15 + bool(0))

var = 1
var +=1
var -=1
print(var)
print(27**(1/3))

# inp = int(input('Введи число\n'))
# print(inp)

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


print(bool("")) 
print(bool(0.0))
print(bool(None))
print(bool("IT Step Academy"))
print(bool(1)) 
print(bool({})) 
print(bool([])) 
print(1 and 8 and 0) 
print(0 or '' or 8 or []) 

car_speed = 100
if 50 < car_speed < 150:
  print("Car is faster than 50 km/h")
elif car_speed == 100:
  print('"---"')
else:
  print('moto')
  
try:
  1/0
except ValueError:
  print("Improper value was obtained")
except Exception as ex:
  print("Hmm... Something went wrong", ex)

# while True:
#   try:
#     apples = int(input("Enter the amount of apples you have: "))
#     if apples < 0:
#       raise Exception("You can’t have -10 apples")
#     parts_number = int(input("Enter the number of parts:"))
#     parts_amount = apples / parts_number
#     print("You have " + str(apples) + " apples \n")
#     print("Each of " + str(parts_number) +
#     " parts consists of " +
#     str(parts_amount) + " apples")
#   except (ZeroDivisionError, ValueError):
#     print("Improper value was obtained")
#   except Exception as ex:
#     print(ex)
#   except:
#     print("Hmm... Something went wrong")


number = 0
while number < 300:
  number += 1
  if number % 3 != 0:
    continue
  elif number % 5 != 0:
    print(number, "divides by 3")
  elif number % 7 != 0:
    print(number, "divides by 3 and 5")
  else:
    print(number, "divides by 3 and 5 and 7")
    
def SumOrMul(event):
  nums = input('3 num split space').split(' ')
  operation = input('operation type (* or +)')
  total = 0

  if operation == '*':
    total = 1

  for n in nums:
    if operation == '+':
      total+=int(n)
    else:
      total*=int(n)
      
  if operation == '+':
    print('sum is', total)
  else:
    print('mul is', total)
    
  
userMessage = 'Hello'
userMessageEnc=userMessage.encode('utf-8') 
print(userMessageEnc)
userMessageDec=userMessageEnc.decode('utf-8')
print(userMessageDec)

myStr="hello"
print(id(myStr)) 
print(type(myStr))
print(myStr)

myStr4='''This is a multi-line string (text). 
This is the first line of text.
This is the second line of text.
This is the third line of text with 'quotes'
'''
 
print(myStr4)

myStr="foobar"
print(myStr[0]) #'f'
print(myStr[1]) #'o'
print(len(myStr)-1) #'r
print(myStr[-1]) #r
print(myStr[-2]) #

# Ошибка. Строки иммутабельны
# myStr[0] = 'z'
# print(myStr) 


str1 = "Hello,"
str2 = "Admin"
print(str1 + str2)
str3 = str1 + str2
print(str3)

myStr="Hello"
print(myStr*5)

myStr = 'fsdfsfsfd'
myStr = myStr.capitalize()
print(myStr)

# ■ str.capitalize() переводит первый символ строки str
# в верхний регистр, остальные — в нижний, возвращаемый результат — преобразованная копия оригинальной строки str (при этом оригинальная строка в 
# результате работы метода не изменится, как и в случае 
# использования рассмотренных ниже методов преобразования регистра).
# ■ str.lower() переводит все буквенные символы оригинальной строки str в нижний регистр, возвращаемый 
# результат — преобразованная копия строки str.
# ■ str.upper() преобразует все буквенные символы строки 
# str в верхний регистр, возвращаемый результат — преобразованная копия строки str.
# ■ str.title() преобразует первые буквы каждого слова в 
# строке str в верхний регистр (а остальные буквы слов 
# переводит в нижний регистр), возвращаемый результат — преобразованная копия строки str.
# ■ str.swapcase() преобразует буквенные символы строки 
# str, меняя их регистр на противоположный, возвращаемый результат — преобразованная копия строки str

# str.count(pattern [, startIndex [, endIndex]]) — определяет 
# количество вхождений фрагмента pattern в строку str
# (или в ее часть при задании диапазона поиска (с индекса startIndex … по индекс endIndex …)

myStr = "Python was created in the late 1980's by Guido van Rossum. Python- cool!"
print(myStr.count('Python')) #2
print(myStr.count('Python',20,65)) #
print(myStr.count('Python',10)) #1

# str.find(pattern [, startIndex [, endIndex]]) — используется для поиска в строке str нужного фрагмента pattern, # возвращаемый результат  — индекс начала первого 
# вхождения фрагмента pattern в строку str или -1 в 
# случае, если фрагмент pattern не входит в состав str.

myStr="Python was created in the late 1980's by Guido van Rossum. Python- cool!"
print(myStr.find('a')) #8
print(myStr.find('a',2,5)) #-1

# str.index(pattern [, startIndex [, endIndex]]) — работа 
# метода аналогична методу .find(), отличие — в вызове 
# исключения ValueError в случае, когда фрагмент pattern
# не найден (не входит в состав str).

# str.rfind(pattern [, startIndex [, endIndex]]) — используется для поиска в строке str нужного фрагмента 
# pattern, начиная с конца строки str, возвращаемый 
# результат  — индекс начала последнего вхождения 
# фрагмента pattern в строку str или -1 в случае, если 
# фрагмент pattern не входит в состав str. Для ограничения диапазона поиска можно использовать параметры 
# startIndex и endIndex.

# str.rindex(pattern [, startIndex [, endIndex]]) работа метода аналогична методу .rfind(), отличие — в вызове # исключения ValueError в случае, когда фрагмент pattern
# не найден (не входит в состав str).


# ?Методы проверки начала (окончания) строк
# str.endswith(pattern [, startIndex [, endIndex]]) — определяет, заканчивается ли строка str указанным фрагментом pattern.
# str.startwith(pattern [, startIndex [, endIndex]]) — определяет, начинается ли строка str с указанного фрагмента 
# pattern.

# Методы проверки строк
# Иногда нужно проверить, состоит ли строка из определенных символов, например, цифр. Для решения такого 
# рода задач предусмотрены следующие методы (все они, 
# как результат, возвращают значение True — если строка 
# содержит нужные символы, False — иначе).
# ■ str.isalnum() — проверяет, состоит ли строка str только 
# из буквенных и цифровых символов.
# ■ str.isalpha() — проверяет, состоит ли строка str только 
# из буквенных символов.
# ■ str.isdigit() — проверяет, состоит ли строка str только 
# из цифровых символов (используется для проверки, 
# является ли строка str числом).
# ■ str.islower() проверяет, находятся ли все буквенные символы строки str в нижнем регистре (символы строки 
# str, которые не являются буквой алфавита — игнорируются данной проверкой).
# ■ str.isspace() проверяет, что в состав строки str входят 
# только пробельные символы, к которым относятся 
# символы пробела ' ', табуляции '\t' и перехода на новую строку '\n'.
# ■ str.istitle() проверяет, начинается ли каждое слово строки str с символа в верхнем регистре.
# ■ str.isupper() определяет, находятся ли все буквенные 
# символы строки str в верхнем регистре.

# Методы форматирования строк
# Методы данной группы изменяют вывод (форматируют) строки.
# !В случае, если параметр width меньше или равен длине строки str, то строка не изменяется.
# ■ str.center(width [, fillchar]) дополняет (расширяет) строку 
# str до указанной длины width, возвращаемый результат — расширенная копия строки str. Если параметр 
# fillchar указан, то он будет использован, как символ 
# заполнения, иначе — отступы заполняются пробелами

# ■ str.expandtabs(tabsize = 8) возвращает копию строки 
# str, в которой каждый символ табуляции ('\t') заменен на пробел, количество которых задается через 
# параметр tabsize

# ■ str.ljust(width [, fillchar]) возвращает выровненную по 
# левому краю копию строки str указанной ширины width

# ■ Для аналогичного выравнивания строки по правому 
# краю в поле указанной ширины используется метод 
# str.rjust(width [, fillchar]).

# ■ str.lstrip([characters]) возвращает копию строки str, 
# удаляя начальные символы (слева), указанные в качестве аргумента characters. Если параметр characters
# не указан, то удаляются символы пробелов.

# ■ Для аналогичного удаления завершающих символов 
# (или пробелов) в строке справа предусмотрен метод 
# str.rstrip([characters]).
# ■ Если необходимо удалить пробелы (или указанные 
# символы) и с левой, и с правой стороны строки, то 
# используется метод str.strip([characters])

# Также для работы со строками предусмотрен интересный метод str.zfill(width), который дополняет строку 
# слева символами «0» ширины width

print ('a'=='a') #True
print (myStr[::1])

print(rf'\n{myStr}\n')

myStr="\001"
print(myStr) # ☺

# Метод replace() возвращает копию строки, в которой все вхождения подстроки заменяются другой подстрокой.
# str.replace(old, new [, count]) 
# Метод в Python может принимать максимум 3 параметра: 
# old ‒ старая подстрока, которую нужно заменить; 
# new ‒ новая подстрока, которая заменит старую подстроку; 
# count (необязательно) ‒ сколько раз вы хотите заменить старую подстроку новой. 
# Примечание: Если число не указано, метод заменяет все вхождения старой подстроки новой.

userLogin = ''.join(random.sample((string.ascii_lowercase),6))
userPass = ''.join(random.sample((string.digits + string.ascii_lowercase + string.digits + string.ascii_uppercase + string.digits), 8))
print("login:",userLogin)
print("password:",userPass)

'[a-zа-я]+'

# Наиболее распространенными и востребованными функциями модуля re для обнаружения совпадений являются:
# ■ re.search(pattern, strObj) — ищет в строке strObj первое 
# совпадение с шаблоном pattern
# ■ re.findall(pattern, strObj) — ищет в строке strObj все 
# (непересекающиеся) совпадения с шаблоном pattern
# (результат — список совпавших с шаблоном строк)
# ■ re.match(pattern, strObj) — ищет в начале строки strObj
# совпадение с шаблоном patter

print(re.search('\w+[@]\w+[.]\w+', 'sdfsd fsdfsd fsdsfwer s1_df@sdfg.ty@sf.df sfwe sdf@d.z rws fsd'))
print(re.findall('\w+[@]\w+[.]\w+', 'sdfsd fsdfsd fsdsfwer s1_df@sdfg.ty@sf.df sfwe sdf@d.z rws fsd'))
print(re.sub('\w+[@]\w+[.]\w+', 'top secret'.upper(), 'sdfsd fsdfsd fsdsfwer s1_df@sdfg.ty sfwe rws fsd'))
print(re.split('\w+[@]\w+[.]\w+', 'sdfsd fsdfsd fsdsfwer s1_df@sdfg.ty sfwe rws sdf@d.z fsd'))
print(re.search('[a-z]+', 'asdfSDAasd'))
print(re.search('[A-Z]+', 'aAsdfSDA'))
print(re.search('[0-9]+', 'asdfSDA'))

# Помимо функций поиска совпадений модуль re предоставляет нам еще такие полезные функции, как re.sub()
# для замены найденных совпадений на новый фрагмент и 
# re.split() для разбиения строки по фрагментам, которые 
# совпадают с шаблоном.

# 1. Определение длины коллекции (количества ее элементов) с помощью встроенной функции len();
print(len([0,1]))
# 2. Проверка принадлежности некоторого элемента к 
# коллекции с помощью оператора принадлежности in;
print(0 in [0,1])
# 3. Обход коллекции с помощью цикла for in;
# 4. Вывод всех элементов коллекции с помощью встроенной функции print().
print([0,1])
print((0,1))

arr = [0,1]
arr1 = arr[:]
arr1.append(3)
print(arr, arr1)

courses = ["Math", "Algorithms", "Databases"]
courses = list(("Math", "Algorithms", "Databases")) # создать список из кортежа

# Генераторы списков
# newList = [expression for item in sequence]

# expression — выражение (вычисление), которое выполняется 
# над каждым элементом item в последовательности sequence. 
# Результат работы генератора — новый список newList

# range(start, end, step)

list1=[i*i for i in range(6)]
print(list1) #[0, 1, 4, 9, 16, 25]

# newList = [expression for item in sequence if condition]

# expression — выражение (вычисление), которое выполняется над 
# таким элементом item в последовательности 
# sequence, для которого condition == True.

list4=[i*i for i in range(1,11) if i%2==0]
print(list4) #[4, 16, 36, 64, 100]

list6 = [x*y for x in range(1, 4) for y in range(1, 4)]
print(list6) #[1, 2, 3, 2, 4, 6, 3, 6, 9]

list7 = [[x*y for x in range(2, 10)] for y in range(2, 10)]
print(list7) #[[4, 6, 8, 10, 12, 14, 16, 18], [6, 9, 12, 15, 18, 21, 24, 27], [8, 12, 16, 20, 24, 28, 32, 36], [10, 15, 20, 25, 30, 35, 40, 45], [12, 18, 24, 30, 36, 42, 48, 54], [14, 21, 28, 35, 42, 49, 56, 63], [16, 24, 32, 40, 48, 56, 64, 72], [18, 27, 36, 45, 54, 63, 72, 81]]

# Для работы со списками можно использовать следующие встроенные Python-функции:
# ■ len(listObj) — возвращает длину списка listObj (количество элементов в списке);
# ■ max(listObj) — возвращает максимальный элемент в 
# списке listObj;
# ■ min(listObj) — возвращает минимальный элемент в 
# списке listObj;
# ■ sum(listObj) — возвращает сумму значений в списке 
# listObj;
# ■ sorted(listObj) — возвращает копию списка listObj, в 
# котором элементы упорядочены по возрастанию (в 
# случае числовых значений) или по алфавиту. Не изменяет оригинальный список listObj.
# Функции max(listObj), min(listObj), sum(listObj) применяются для списков, содержащих числовые значен

print(max(['a','b','-','B', 'в']))
print(sum([i for i in range(1,4)]))

# Цикл с доступом к индексам
category =["Drama", "Comedy", "Mystery", "Romance"]
for i in range(len(category)):
  print(category[i], i)
  
for el in category:
  print(el)
  
  
# Метод listObj.append(item) позволяет добавить еще 
# один элемент (аргумент метода, item) в конец списка listObj.

# Метод listObj.extend(list) позволяет добавить в listObj 
# все элементы списка list в конец списка listObj.

category.extend(['Horror','Anime'])
print(category) #['Drama', 'Comedy', 'Mystery', 'Romance', 'Horror', 'Anime']

# Метод listObj.insert (itemIndex, item) вставляет указанный 
# элемент item в список listObj по указанному индексу itemIndex

# Метод listObj.remove(item) удаляет первое вхождение 
# указанного значения (item) в списке.

category.append('Horror')
category.remove('Horror')

print(category)

# Метод listObj.pop(itemIndex) удаляет элемент по указанному 
# (itemIndex) значению индекса. При использовании данного 
# метода без аргументов будет удален последний элемент в списке listObj

# Метод listObj.clear() удаляет все элементы из списка listObj.

# Если необходимо определить позицию элемента в 
# списке listObj по его значению (item), то используется 
# метод listObj.index(item)
# !метод index() возвращает только первое вхождение элемента

# Если необходимо определить, сколько раз определенное 
# значение item встречается в списке listObj, то используем 
# метод listObj.count(item)

# Ранее нами уже была рассмотрена встроенная функция 
# sorted(), которая возвращала отсортированную копию 
# списка. 
# Также есть метод списка listObj.sort(reverse= False) с 
# аналогичной функциональностью, который по умолчанию 
# сортирует список по возрастанию (т.к у параметра reverse
# значение по умолчанию False). Если необходимо изменить 
# направление сортировки (сортировать по убыванию), то 
# следует установить reverse= True.
# Метод listObj.reverse() меняет порядок сортировки 
# элементов на обратный

# Если необходимо проверить, ссылаются ли две разные 
# переменные на один и тот же список, то можно использовать 
# следующий подход с помощью оператора is, 
# который проверяет, являются ли две переменный одним 
# и тем же объектом

list1=[1,2,3,4,[5]]
list2=[1,2,3,4,[5]]
list3=[6,7,8]
print(list2 is list1) #False
print(list2 == list1) #True
print(list3 is list1) #False

# Варианты копирования списка
listZ = list1.copy()
listX = list1[:]
listC = list(list1)

# Именно для таких ситуаций и предназначен метод 
# listObj.index(item, start, stop) который возвращает позицию элемента 
# item при его первом появлении в списке listObj

def isPalindrom(string):
  string = string.lower()
  reverseStr = list(string)
  reverseStr.reverse()
  return string == ''.join(reverseStr)

def isPalindrom1(string):
  str1 = ''
  string = string.lower()
  for char in string:
    str1 = char+str1
  return string == str1

def isPalindromBest(string):
  string = string.lower()
  string = string.replace(' ', '')
  l = len(string)
  for i in range(l//2):
    if string[i]!=string[l-1-i]:
      return False
  return True
    
print(isPalindromBest('string'))
print(isPalindromBest('А буду я у дуба'))

list1 = [1,2,3,4]
list2 = [5,6,7,8]


# https://pythonworld.ru/tipy-dannyx-v-python/vse-o-funkciyax-i-ix-argumentax.html

def myFunc(name, *args, **kvargs):
  print('hello '+ name)
  return 'hello '+ name
  
  
print('func return ',myFunc('student', 1, 2, 3))

def newfunc(n:int)->int:
    def myfunc(x):
        return n + x
    return myfunc
  
addTo4 = newfunc(4)
print(addTo4)
print(addTo4(2))
print(newfunc(4)(5))
print(newfunc('hello ')('world'))

def func1():
  pass

def func2():
  func1()

def func(a, b, c=2, *args): # c - необязательный аргумент
  return a + b + c + sum(args)

print(func(1,2))
print(func(1,2,3))
print(func(b=6,a=0))
# print(func(1,a=2))
print(func(1,2,3,4,5,6,7,8))

def func(*args,**kwargs):
    print(args)
    print(kwargs)

func (a=1,b=2)
func (1,2)
func (1,2,a=1,b=2)

print((lambda x, y: x + y)(1, 2))
func = lambda x, y: x + y
print (func(5,9))

def map(list:list, func):
  for i in range(len(list)):
    list[i] = func(list[i], i)
  return list
    
print(map([1,2,3,4,5], lambda el, i: el+1))
print(map([1,2,3,4,5], lambda el, i: el+i))


def someFunc():
  def sum(a,b):
    pass
  print(sum(1,2))
  
someFunc()

def factorial(n:int)->int:
  if n == 1:
    return n
  return n*factorial(n-1)

# 5!
# 1*2*3*4*5

print(factorial(5))

def printFugure()->None:
  variant = input('Ведите вариант от "а" до "к"')
  lenght = int(input('Ведите нечётное число'))
  string = ''
  for y in range(lenght):
    for x in range(lenght):
      match variant:  
        case 'а':  
          if y<=x:
            string+=' * '
          else:
            string+='   '
        case 'б':
          if y>=x:
            string+=' * '
          else:
            string+='   '
        case 'в':
          if y<=x and y<=lenght-x-1:
            string+=' * '
          else:
            string+='   '
        case 'г':
          if y>=lenght-x-1 and y>=x:
            string+=' * '
          else:
            string+='   '  
        case 'д':
          if (y>=lenght-x-1 and y>=x) or (y<=x and y<=lenght-x-1):
            string+=' * '
          else:
            string+='   '    
        case 'е':
          if (y>=x and y<=lenght-x-1) or (y<=x and y>=lenght-x-1):
            string+=' * '
          else:
            string+='   '  
        case 'ж':
          if y>=x and y<=lenght-x-1:
            string+=' * '
          else:
            string+='   '
        case 'з':
          if y<=x and y>=lenght-x-1:
            string+=' * '
          else:
            string+='   '  
        case 'и':
          if y<=lenght-x-1:
            string+=' * '
          else:
            string+='   '
        case 'к':
          if y>=lenght-x-1:
            string+=' * '
          else:
            string+='   ' 
        case _:
          pass
    string += '\n'
  print(string)
    
    
# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны ква-
# драта, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой.

def printSquere(lenght:int, simbol:str, fill:bool)->None:
  l = lenght+2
  s = ''
  for x in range(l):
    for y in range(l):
      if x==0 or x==l-1:
        if y==0:
          s+= ' -'
        elif y==l-1:
          s+= ''
        else:
          s+= '--'
      else:
        if y==0 or y==l-1:
          if y==0:  
            s+= '|'
          if y==l-1:
            s+= ' |'
        else:
          if fill:        
            s+= ' '+simbol
          else:
            s+= '  '
    s+='\n'
  print(s)
  
# printSquere(15, '*', True)
# l = int(input('Введите сторону квадрата'))
# s = input('Введите символ')
# z = bool(int(input('Закрашивать? (0,1)')))
# printSquere(l, s, z)  

def DZ5_3_5_bulls_and_cows():
  # Написать игру «Быки и коровы». Программа «за-
  # гадывает» четырёхзначное число и играющий должен
  # угадать его. После ввода пользователем числа программа
  # сообщает, сколько цифр числа угадано (быки) и сколько
  # цифр угадано и стоит на нужном месте (коровы). После
  # отгадывания числа на экран необходимо вывести коли-
  # чество сделанных пользователем попыток. В программе
  # необходимо использовать рекурсию.
  num = ''.join(random.sample(string.digits, 4))
  count = 0
  print(num)
  def recurcive(num, count):
    count+=1
    userNum = input('Угадай число: ')
    cows = 0
    bulls = 0
    newUserNum = ''
    for n in userNum:
      if n not in newUserNum:
        newUserNum += n
    for n in newUserNum:
      if (n in num):
        bulls+=1
    for i in range(4):
      if num[i]==userNum[i]:
        cows+=1
    if userNum != num:
      print('Bulls: '+str(bulls)+'. Cows: '+ str(cows))
      recurcive(num, count)
    else:
      print('Congrats! I\'s takes ' + str(count) + ' trys')
  recurcive(num, count)
  
# DZ5_3_5_bulls_and_cows()


# !Основные моменты
# ?1. Список — это тип данных в Python, используемый для хранения нескольких объектов. Это упорядоченная и изменяемая коллекция разделенных запятыми элементов в квадратных скобках, например:
myList = [1, None, True, "I am a string", 256, 0]

# ?2. Списки могут быть проиндексированы и обновлены, например:
myList = [1, None, True, 'I am a string', 256, 0]
print(myList[3]) # выводит: I am a string
print(myList[-1]) # выводит: 0 
myList[1] = '?' 
print(myList) # выводит: [1, '?', True, 'I am a string', 256, 0] 
myList.insert(0, "first") 
myList.append("last") 
print(myList) # выводит: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']

# ?3. Списки могут быть вложенными, например: 
myList = [1, 'a', ["list", 64, [0, 1], False]]

# ?4. Элементы списка и списки могут быть удалены, например:
myList = [1, 2, 3, 4] 
del myList[2] 
print(myList) # выводит: [1, 2, 4] 
del myList # удаляет весь список

# ?5. Списки можно перебирать, используя цикл for, например:
myList = ["white", "purple", "blue", "yellow", "green"]
for color in myList: 
 print(color)

# ?6. Функция len() может использоваться для проверки длины списка, например:
myList = ["white", "purple", "blue", "yellow", "green"]
print(len(myList)) # выводит 5 
del myList[2] 
print(len(myList)) # выводит 4

# ?7. Типичный вызов функции выглядит следующим образом: 
# result = function(arg), а типичный вызов метода 
# выглядит так: result = data.method(arg).

var1 = 1 
var2 = 2 
print(var1, var2)
var1, var2 = var2, var1
print(var1, var2)


myList = [10, 1, 8, 3, 5] 
myList[0], myList[4] = myList[4], myList[0] 
myList[1], myList[3] = myList[3], myList[1] 
print(myList)

print(sorted("This is a test string from Andrew".split(), key=str.casefold))
print(sorted("This is a test string from Andrew".split()))
myArr = "This is a test string from Andrew".split()
myArr.sort(key=str.casefold)
print(myArr)
myArr.sort()
print(myArr)

myList = [999999.5,8, 10, 6, 2, 4,12,54,23,5,123,35,4,631265,45643,21,35,6] # список для сортировки 

# Сортировка пузырьком
def bubble(myList):
  swapped = True # небольшое жульничество – 
  # нам необходимо ввести цикл while
  numStartFromBegin = 0
  numSwapped = 0
  while swapped: 
    numStartFromBegin += 1
    swapped = False # никакого обмена местами
    for i in range(len(myList) - 1):
      if myList[i] > myList[i + 1]: 
        numSwapped += 1
        swapped = True # произошёл обмен местами! 
        myList[i], myList[i + 1] = myList[i + 1], myList[i] 
  # print(myList, numStartFromBegin, numSwapped, len(myList))

myList.sort(reverse=False)
print(myList)

# Бинарный поиск

a = myList
value = 35
left = 0
right = len(a) - 1

while left <= right:
    center = (left + right) // 2
    if value == a[center]:
        print('ID =', center)
        break
    if value > a[center]:
        left = center + 1
    else:
        right = center - 1
else:
    print('No value')


# Метод вставок

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        x = array[i]
        j = i

        while j > 0 and array[j - 1] > x:
            array[j] = array[j - 1]
            j -= 1

        array[j] = x

    return array


# insertion_sort([6, 5, 3, 8, 9, 1]) # [1, 3, 5, 6, 8, 9]



def merge_sort(L):
  if len(L) < 2:
      return L[:]
  else:
      middle = int(len(L) / 2)
      left = merge_sort(L[:middle])
      right = merge_sort(L[middle:])
      return merge(left, right)
      
def merge(left, right):
  result = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
      if left[i] < right[j]:
          result.append(left[i])
          i += 1
      else:
          result.append(right[j])
          j += 1
  while i < len(left):
      result.append(left[i])
      i += 1
  while j < len(right):
      result.append(right[j])
      j += 1
  return result

print(merge_sort([6, 5, 3, 8, 9, 1])) # [1, 3, 5, 6, 8, 9]

def shell(list):
    n = len(list)
    d = n // 2
    while d > 0:
        for i in range(d, n):
            j = i
            t = list[i]
            while j >= d and list[j - d] > t:
                list[j] = list[j - d]
                j -= d
            list[j] = t
        d //= 2
    return list
  
print(shell([6, 5, 3, 8, 9, 1])) # [1, 3, 5, 6, 8, 9]


def heapify(nums, heap_size, root_index):  
    # Индекс наибольшего элемента считается корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня — это допустимый индекс, а элемент больше,
    # чем текущий наибольший, то мы обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
      largest = left_child

    # То же самое и для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
      largest = right_child

    # Если наибольший элемент уже не корневой, они меняются местами
    if largest != root_index:
      nums[root_index], nums[largest] = nums[largest], nums[root_index]
      heapify(nums, heap_size, largest)

def heap_sort(nums):  
    n = len(nums)

    # Создаём Max Heap из списка
    # 2-й аргумент означает остановку алгоритма перед элементом -1, то есть
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении, 
    # уменьшая счётчик i на 1 
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Перемещаем корень Max Heap в самый конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

# Проверяем, что всё работает
random_list_of_nums = [35, 12, 43, 8, 51]  
heap_sort(random_list_of_nums)  
print(random_list_of_nums)

# https://habr.com/ru/articles/188010/
# https://habr.com/ru/articles/782608/


def quicksort(nums):
  if len(nums) <= 1:
    return nums
  else:
    q = random.choice(nums)
  l_nums = [n for n in nums if n < q]
  e_nums = [q] * nums.count(q)
  b_nums = [n for n in nums if n > q]
  return quicksort(l_nums) + e_nums + quicksort(b_nums)

random_list_of_nums = [35, 12,12, 43,8, 8, 51]  
quicksort(random_list_of_nums)  
print(random_list_of_nums)

# sortTime = 0
# insertionTime = 0
# mergeTime = 0
# shellTime = 0
# heapTime = 0 
# quickTime = 0
# mainStart = time.time()
# for i in range(100):
#   A = [random.randint(1, 10000) for i in range(10000)]

#   a1 = A[:]
#   start = time.time()
#   a1.sort()
#   end = time. time()
#   sortTime += end-start

#   # a2 = A[:]
#   # start = time.time()
#   # bubble(a2)
#   # end = time. time()

#   # print ('bubble', end-start)

#   a3 = A[:]
#   start = time.time()
#   insertion_sort(a3)
#   end = time. time()

#   insertionTime += end-start

#   a4 = A[:]
#   start = time.time()
#   merge_sort(a4)
#   end = time. time()

#   mergeTime += end-start

#   a5 = A[:]
#   start = time.time()
#   shell(a5)
#   end = time. time()

#   shellTime += end-start

#   a6 = A[:]
#   start = time.time()
#   heap_sort(a6)
#   end = time. time()

#   heapTime += end-start

#   a7 = A[:]
#   start = time.time()
#   quicksort(a7)
#   end = time. time()
  
#   quickTime += end-start
  
#   print(i)

# print ('sort', sortTime/1000)
# print ('insertion_sort', insertionTime/1000)
# print ('merge_sort', mergeTime/1000)
# print ('shell', shellTime/1000)
# print ('heap_sort', heapTime/1000)
# print ('quicksort', quickTime/1000)
# print ('all', time.time()-mainStart)

# ?Кортежи
# https://metanit.com/python/tutorial/3.2.php
tom = ("Tom", 37, "Google", "software developer")
# !'tuple' object does not support item assignment
# tom[0] = "NotTom"

name, age, company, position = ("Tom", 37, "Google", "software developer")
print(tom[1:3])

def print_person(name, age, company):
  print(f"Name: {name}  Age: {age}  Company: {company}")
 
tom = ("Tom", 22)
print_person(*tom, "Microsoft")     # Name: Tom  Age: 22  Company: Microsoft
 
bob = ("Bob", 41, "Apple")
print_person(*bob)      # Name: Bob  Age: 41  Company: Apple

print(list(bob))


# ?Словари
# https://metanit.com/python/tutorial/3.3.php

users = {1: "Tom", 2: "Bob", 3: "Bill"}
emails = {"tom@gmail.com": "Tom", "bob@gmai.com": "Bob", "sam@gmail.com": "Sam"}

users_list = [
    ["+384767557", "Bob"],
    ["+958758767", "Alice"],
]
users_dict = dict(users_list)
print(users_dict) 
# !Нет ключа KeyError
# user = users_dict["+4444444"]

key = "+4444444"
if key in users_dict:
    user = users_dict[key]
    print(user)
else:
    print("Элемент не найден")
    
# get(key): возвращает из словаря элемент с ключом key. Если элемента с таким ключом нет, то возвращает значение None

# get(key, default): возвращает из словаря элемент с ключом key. Если элемента с таким ключом нет, то возвращает значение по умолчанию default

print(users_dict.get("+4444444"))
print(users_dict.get("+4444444", None))
del users_dict["+384767557"]
print(users_dict)

# pop(key): удаляет элемент по ключу key и возвращает удаленный элемент. Если элемент с данным ключом отсутствует, то генерируется исключение KeyError

# pop(key, default): удаляет элемент по ключу key и возвращает удаленный элемент. Если элемент с данным ключом отсутствует, то возвращается значение default

# Если необходимо удалить все элементы, то в этом случае можно воспользоваться методом clear():
# users.clear()

users = users_dict
users["+465413"]="dsfsdf"
print(users)
print(users_dict)

# Метод copy() копирует содержимое словаря, возвращая новый словарь:
users1 = users_dict.copy()
users1["+465413"]="SDFDSFDS"
users1["+465413d"]="dsfsdfdfgdf"
print(users1)
print(users_dict)

# Метод update() объединяет два словаря:
users_dict.update(users1)
print(users_dict)

# При этом словарь users1 остается без изменений. Изменяется только словарь users, в который добавляются элементы другого словаря. Но если необходимо, чтобы оба исходных словаря были без изменений, а результатом объединения был какой-то третий словарь, то можно предварительно скопировать один словарь в другой:

# users2 = users_dict.copy()
# users2.update(users1)

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key in users:
    print(f"Phone: {key}  User: {users[key]} ")

users = {
  "+11111111": "Tom",
  "+33333333": "Bob",
  "+55555555": "Alice"
}
for key, value in users.items():
    print(f"Phone: {key}  User: {value} ")
    
for key in users.keys():
    print(key)
    
for value in users.values():
    print(value)
    
print(users.items())
print(users.keys())
print(users.values())

users = {
    "Tom": {
        "name": "Tom",
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Bob": {
        "phone": "+876390444",
        "email": "bob@gmail.com",
        "skype": "bob123"
    }
}

userList = (
  {"name": "Tom", "phone": "+971478745", "email": "tom12@gmail.com"},
  {"name": "Bob", "phone": "+876390444", "email": "bob@gmail.com", "skype": "bob123"}
)

userList[1]['name'] = 'NotBob'
userList[1]['name1'] = 'Bobby'
print(userList)

old_email = users["Tom"]["email"]
users["Tom"]["email"] = "supertom@gmail.com"
print(users["Tom"]) 

# ?Множества
# https://metanit.com/python/tutorial/3.4.php

users = {"Tom", "Bob", "Alice", "Tom"}
print(users)    # {"Alice", "Bob", "Tom"}

people = ["Mike", "Bill", "Ted"]
users = set(people)
print(users)    # {"Mike", "Bill", "Ted"}

# Функцию set удобно применять для создания пустого множества:
users = set()
print(len(users))
users.add("Sam")
users.add("Sam")
users.add("Sam")
users.add("Sam")
print(users)
user = "Tom"
if user in users: 
    users.remove(user)
print(users)

# Удаляет элемент, если он есть, не вызывая ошибки
users.discard("Tim")
users.discard("Tom")
users.discard("Tam")
print(users)

# Для удаления всех элементов вызывается метод clear():
users.clear()

users = {"Tom", "Bob", "Alice"}
 
for user in users:
    print(user)
    
users = {"Tom", "Bob", "Alice"}
students = users.copy()
print(students)     # {"Tom", "Bob", "Alice"}


# try: 
#   stream = open('./text.txt', "at")
#   stream.write('New string\n')
#   stream.close()
# except Exception as exc: 
#   print("Cannot open the file:", exc)


try: 
  for line in open('./text.txt', "rt"):
    print(line, end='')
except Exception as exc: 
  print("Cannot open the file:", exc)



data = bytearray(10) 

for i in range(10):
  data[i] = 10-i

try: 
  bf = open('file.bin', 'wb') 
  bf.write(data) 
  bf.close() 
except IOError as e: 
  print("I/O error occurred:", e)


try: 
  bf = open('file.bin', 'rb') 
  bf.readinto(data) 
  bf.close() 
  for b in data: 
    print(hex(b), end=' ') 
except IOError as e: 
  print("I/O error occurred:", e)
  
print(dir(m))

from random import random, seed 
seed(0)
for i in range(5): 
 print(random())
 
import platform

print(platform.platform(aliased = False, terse = False))
print(platform.machine())
print(platform.processor())
print(platform.python_version_tuple())

import module
print(module.fix)
print(module._notChange)
module._notChange = 15
print(module._notChange)
print(module.hello())

import sys

print (sys.path)
sys.path.append('c:\\Users\\N.Gakman\\Documents\\python35\\extra.zip')

from extra.good.alpha import FunA # type: ignore

def powersOf2(n): 
 pow = 1 
 for i in range(2,n+1): 
  yield pow 
  pow *= i 
t = [x for x in powersOf2(5)] 
print(t)

def powersOf2(n): 
 pow = 1 
 for i in range(n): 
  yield pow 
  pow *= 2 
for i in range(20): 
 if i in powersOf2(4): 
  print(i)
  
def Fib(n): 
 p = pp = 1 
 for i in range(n): 
  if i in [0, 1]: 
    yield 1 
  else: 
    n = p + pp 
    pp, p = p, n 
    yield n 
fibs = list(Fib(77)) 
print(fibs)


def outer(par): 
 loc = {"par": par} 
 def inner(): 
   loc['par'] = loc['par']+1 
   return loc['par']
 return inner 
 
var = 1 
fun = outer(var) 
print(fun())
print(fun())
print(fun())
print(fun())

# a0ddfabdd36caf357cfdb47776f460ffc5bae5ee

class TheSimplestClass: 
  pass

myObj = TheSimplestClass()
myObj1 = TheSimplestClass()
myObj2 = TheSimplestClass()
print(type(myObj))

class Stack: 
  def __init__(self): 
    self.__stackList = []
    
  def push(self, val): 
    self.__stackList.append(val) 
    
  def pop(self): 
    val = self.__stackList[-1] 
    del self.__stackList[-1] 
    return val 
    
class AddingStack(Stack):
  def __init__(self):
    Stack.__init__(self)
    self.__sum = 0    
  
  def push(self, val): 
    Stack.push(self, val)  
    self.__sum += val 

  def getSum(self): 
    return self.__sum

  def pop(self): 
    val = Stack.pop(self) 
    self.__sum -= val 
    return val
  
sumStack = AddingStack() 
sumStack.push(3)
sumStack.push(3)
sumStack.push(3)
print('SL', sumStack._Stack__stackList)
print(sumStack.getSum())
sumStack.pop()
print(sumStack.getSum())
  
stackObject = Stack() 
stackObject2 = Stack() 
stackObject.push(3)
stackObject.push(2)
stackObject.push(1)
print(stackObject.__dict__) 
print(stackObject.pop())
print(stackObject.pop())
print(stackObject.pop())

class ExampleClass: 
  def __init__(self, val = 1): 
    self.__first = val 
  
  @property
  def second(self): 
    return self.__second
  
  @second.setter
  def second(self, val): 
    self.__second = val 
  
exampleObject1 = ExampleClass() 
exampleObject2 = ExampleClass(2) 
exampleObject2.second = 3
exampleObject3 = ExampleClass(4) 
exampleObject3.__third = 5
print('***************')
if hasattr(exampleObject3, '_ExampleClass__first'): 
 print(exampleObject3._ExampleClass__first)
print('***************')
exampleObject1.__second = 10
exampleObject1.second = 10
exampleObject1.__dict__['_ExampleClass__second'] = 11
print(exampleObject1.__dict__) 
print(exampleObject1.second) 
print(exampleObject2.__dict__) 
print(exampleObject3.__dict__)

class ExampleClass: 
  counter = 0 
  def __init__(self, val = 1): 
    self.__first = val 
    ExampleClass.counter += 1 
    self.id = ExampleClass.counter
    
exampleObject1 = ExampleClass() 
exampleObject2 = ExampleClass(2) 
exampleObject3 = ExampleClass(4) 
print(ExampleClass.__dict__)
print(exampleObject1.__dict__, exampleObject1.id, exampleObject1.counter, ExampleClass.counter)
print(exampleObject2.__dict__, exampleObject2.id, exampleObject2.counter, ExampleClass.counter)
print(exampleObject3.__dict__, exampleObject3.id, exampleObject3.counter, ExampleClass.counter)


class ExampleClass:
 varia = 1
 def __init__(self, val):
    ExampleClass.varia = val

print(ExampleClass.__dict__)
exampleObject = ExampleClass(2)
print(ExampleClass.__dict__)
print(exampleObject.__dict__)

class ExampleClass: 
 a = 1 
 def __init__(self): 
  self.b = 2 
exampleObject = ExampleClass() 
print(hasattr(exampleObject, 'b')) 
print(hasattr(exampleObject, 'a')) 
print(hasattr(ExampleClass, 'b')) 
print(hasattr(ExampleClass, 'a'))

print(ExampleClass.__name__)
print(type(exampleObject).__name__)

class SuperOne:
  staticProp = 1
  @staticmethod
  def myStatic():
    return SuperOne.staticProp
  
class SuperTwo:
 pass
class Sub(SuperOne, SuperTwo):
 pass

class Sub1(SuperOne):
 pass

class Sub2(Sub1):
 pass

def printBases(cls):
 print('( ', end='')
 for x in cls.__bases__:
  print(x.__name__, end=' ')
 print(')')
 
 
printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)
print(Sub1.__bases__)
print(Sub2.__bases__)
print(Sub2.__bases__[0].__bases__)

# определение функции декоратора
def select(input_func):    
    def output_func():      # определяем функцию, которая будет выполняться вместо оригинальной
        print("*****************")  # перед выводом оригинальной функции выводим всякую звездочки
        input_func()                # вызов оригинальной функции
        print("*****************")  # после вывода оригинальной функции выводим всякую звездочки
    return output_func     # возвращаем новую функцию
 
# определение оригинальной функции
# @select         # применение декоратора select
def hello():
    print("Hello METANIT.COM")
 
# вызов оригинальной функции
hello()

def logDecorator(f):
  def inner(*args):
    res = f(*args)
    print('log decorator', 'args', args, 'res=', res)
    return res
  return inner

@logDecorator
def sum(a,b):
  return a+b

print(sum(1,5))

print(SuperOne.myStatic())
superObj = SuperOne()
print(superObj.myStatic())

def iter():
  for i in range(10):
    yield i
    
# for i in iter():
#   print(i)
# for i in iter():
#   print(i)

# Создайте класс Complex (комплексное число). Более
# подробно ознакомиться с комплексными числами можно
# по ссылке.
# Создайте перегруженные операторы для реализации
# арифметических операций для по работе с комплексными
# числами (операции +, -, *, /)

class Complex:
  def __init__(self, real, imag):
    self.real = real
    self.imag = imag
  def __repr__(self) -> str:
    return str(self.real) + ('+' if self.imag>=0 else '') + str(self.imag) + 'i'
  def __add__(self, other):
    return Complex(self.real + other.real,self.imag + other.imag)
  def __sub__(self, other):
    return Complex(self.real - other.real,self.imag - other.imag)
  def __mul__(self, other):
    return Complex(self.real * other.real + self.imag * other.imag * -1 ,self.real * other.imag+self.imag * other.real)
  def __truediv__(self, other):
    z3 = Complex(other.real, -other.imag)
    delitel = (z3*other).real
    z4 = z3*self
    return Complex(z4.real/delitel ,z4.imag/delitel)
    
z1 = Complex(-4,2)
z2 = Complex(1,-3)
print(z1,z2)
print(z1+z2)
print(z1-z2)
print(z1*z2)
print(z1/z2)

class ListData:
  def __init__(self, data):
    self.data = data
    self.next = None
    
class OneWayList:
  def __init__(self):
    self.index=-1
    self.start=None
    self.end=None    
  def add(self, data):
    newData = ListData(data)
    if self.start == None:
      self.start = newData
    if self.end == None:
      self.end = newData
    else:
      self.end.next = newData
      self.end = newData
    self.index += 1
  def showList(self):
    list = self.start
    while list.next != None:
      print(list.data)   
      list = list.next
    print(list.data)   
  def checkKey(self, key):
    if isinstance(key, int):
      if key<0 or key>self.index:
        raise KeyError
    else:
      raise KeyError
  def __getitem__(self, key):
    self.checkKey(key)
    list = self.start
    i = 0
    while i<key:
      list = list.next
      i+=1
    return list.data  
  def __setitem__(self, key, value):
    self.checkKey(key)
    list = self.start
    i = 0
    while i<key:
      list = list.next
      i+=1
    list.data = value
  def __delitem__(self, key):
    self.checkKey(key)
    if key==0:
      self.start = self.start.next
    else:
      list = self.start
      i = 0
      while i<key-1:
        list = list.next
        i+=1
      if key==self.index:
        list.next = None
        self.end = list
      else:  
        list.next = list.next.next
    self.index -=1
    
    
      
myList = OneWayList()
myList.add(1)
myList.add(2)
myList.add(3)
myList.add(4)

print('index',myList.index)
del myList[0] 
print('index',myList.index)
del myList[2] 
print('index',myList.index)

myList.add(55)

print('index',myList.index)
myList.showList()


class ListData:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
    
class TwoWayList:
  def __init__(self):
    self.start=None
    self.end=None    
  def append(self, data):
    newData = ListData(data)
    if self.start == None:
      self.start = newData
    if self.end == None:
      self.end = newData
    else:
      self.end.next = newData
      newData.prev = self.end
      self.end = newData
  def prepend(self, data):
    newData = ListData(data)
    if self.start == None:
      self.start = newData
    if self.end == None:
      self.end = newData
    else:
      newData.next = self.start
      self.start.prev = newData
      self.start = newData
  def showListForvard(self):
    list = self.start
    while list.next != None:
      print(list.data)   
      list = list.next
    print(list.data)   
  def showListBackvard(self):
    list = self.end
    while list.prev != None:
      print(list.data)   
      list = list.prev
    print(list.data)   
      
myList = TwoWayList()
myList.append(2)
myList.append(3)
myList.append(4)
myList.prepend(1)
myList.append(5)
myList.append(6)

print('forvard')
myList.showListForvard()
print('backvard')
myList.showListBackvard()

# LIFO append, pop
# FIFO append, pop(0)

class Leaf:
  def __init__(self, data):
    self.parent = None
    self.left = None
    self.right = None
    self.data = data
  def __repr__(self):
      return '('+('NONE' if self.left==None else str(self.left.data)) + ';' + str(self.data) + ';' +('NONE' if self.right==None else str(self.right.data)) +')'

    
class Tree:
  def __init__(self):
    self.head = None
  @staticmethod
  def find(el, data):
    if data > el.data:
      if el.right == None:
        return el
      else:
        return Tree.find(el.right, data)
    elif data < el.data:
      if el.left == None:
        return el
      else:
        return Tree.find(el.left, data)
    else:
        return el
      
  def add(self, data):
    if self.head == None:
      self.head = Leaf(data)
    else:
      el = Tree.find(self.head, data)
      if el.data == data:
        print ('jest')
      else:
        if data > el.data:
          el.right = Leaf(data)
        else:
          el.left = Leaf(data)
    

myTree = Tree()
myTree.add(5)
myTree.add(10)
myTree.add(3)
myTree.add(100)
myTree.add(15)
myTree.add(50)
myTree.add(60)
myTree.add(1100)
myTree.add(20)
myTree.add(38)
myTree.add(14)
myTree.add(49)

print(Tree.find(myTree.head, 39))
print('_______')

print(myTree.head)
print(myTree.head.left)
print(myTree.head.right)
print(myTree.head.right.right)
print(myTree.head.right.right.left)
print(myTree.head.right.right.left.right)
print(myTree.head.right.right.left.right.left)
print(myTree.head.right.right.left.right.right)
print(myTree.head.right.right.right)

class Instrument:
  pass

class Musician:
  pass

class Violin(Instrument):
  pass
    
class Cello(Instrument):
  pass
    
class Violinist(Musician):
  pass
    
class Cellist(Musician):
  pass

class ReservationFactory:
  def reserveInstrument() -> Instrument:
    pass
  def notifyPlayer() -> Musician:
    pass

class ViolinReservation(ReservationFactory):
  def reserveInstrument() -> Violin:
    pass
  def notifyPlayer() -> Violinist:
    pass

class CelloReservation(ReservationFactory):
  def reserveInstrument() -> Cello:
    return Cello()
  def notifyPlayer() -> Cellist:
    return Cellist()
  
def reserve(reservation: ReservationFactory) -> tuple:
  return (reservation.notifyPlayer(), reservation.reserveInstrument())

reserve(ViolinReservation)
reserve(CelloReservation)


class Singleton:
  __instance = None
  def __new__(cls, *args, **kwargs):
    if cls.__instance is None:
      cls.__instance = super().__new__(cls)
    return cls.__instance
  def __init__(self, val):
    if not hasattr(self, 'val'):
      self.val = val
      
print (Singleton(None).val)
print (Singleton(20).val)
print (Singleton(20) == Singleton(40))

class Drink:
  def __init__(self, settings):
    self.base = settings['base']
    self.milk = settings['milk']
    self.sugar = settings['sugar']
    self.cream = settings['cream']
    self.syrup = settings['syrup']

class DrinkBuilder:
  settings = {
    'base': 1,
    'milk': 0,
    'sugar': 0,
    'cream': 0,
    'syrup': 0,
  }
  
  def addBase(self):
    self.settings['base'] += 1
    return self

  def addMilk(self):
    self.settings['milk'] += 1
    return self

  def addSugar(self):
    self.settings['sugar'] += 1
    return self

  def addCream(self):
    self.settings['cream'] += 1
    return self

  def addSyrup(self):
    self.settings['syrup'] += 1
    return self

  def build(self):
    return Drink(self.settings)

print(DrinkBuilder().addBase().addMilk().addSyrup().addSyrup().build().__dict__)

def dz77():
  i = 0
  while True:
    print (i)
    i+=1
    if (i>50):
      break

# dz77()

class Point:
  def __init__(self, x,y):
    self.x = x
    self.y = y
  def clone(self):
    return Point(self.x, self.y)
  # def __repr__(self) -> str:
  #   return f'({self.x},{self.y})'

class Shape(ABC):
  @abstractmethod
  def clone(self):
    pass
  
class Rectangle(Shape):
  def __init__(self, p1:Point, p2:Point):
    self.p1 = p1 
    self.p2 = p2
  def clone(self):
    return Rectangle(self.p1.clone(),self.p2.clone())
 
class Circle(Shape):
  def __init__(self, p:Point, r:float):
    self.p = p 
    self.r = r 
  def clone(self):
    return Circle(self.p.clone(),self.r)
  
myRect = Rectangle(Point(0,0), Point(5,3))
myRectClone = myRect.clone()
print(myRect,myRect.__dict__)
print(myRectClone,myRectClone.__dict__)
myRect.p1.x = 90
print(myRectClone.p1.x)

import datetime


class LogToFile:
  def __init__(self, fileName):
    self.fileName = fileName
  def log(self, *args):
    print('log to file', datetime.datetime.now(), *args)

class LogToDisplay:
  def log(self, *args):
    print('log to display', *args)

class Logger:
  def __init__(self, logObject):
    self.logObject = logObject
  def log(self, *args):
    self.logObject.log(*args)

# init
logger = Logger(LogToFile('calc.log'))

class Calc:
  def __init__(self):
    self.x=0
  def add(self, x):
    self.log(self.x, 'add', x)
    self.x+=x
  def mul(self, x):
    self.log(self.x, 'mul', x, '***not use in prod***')
    self.x+=x
  def log(self, *args):
    logger.log(*args)
    
c1 = Calc()

c1.add(3)
c1.add(5)
c1.add(10)

c2 = Calc()

c2.add(38)
c2.add(15)
c2.add(-10)
c2.mul(3)

class DataSource:
    def writeData(self, data):
      pass
    def readData(self):
      pass


class FileDataSource(DataSource):
    def __init__(self, filename):
      self.filename = filename
      self.data = ''
    def writeData(self, data):
      self.data = data
      print(f'В файл {self.filename} записано {data}')
    def readData(self):
      print(f'Из файла {self.filename} прочитано {self.data}')
      return self.data

class DataSourceDecorator(DataSource):
    def __init__(self,source: DataSource):
        self.wrappee = source
    def writeData(self,data):
        self.wrappee.writeData(data)
    def readData(self):
        return self.wrappee.readData()

class EncryptionDecorator(DataSourceDecorator):
    def writeData(self,data):
        data = '***' + data + '***'
        super().writeData(data)
        #  1. Зашифровать поданные данные.
        #  2. Передать зашифрованные данные в метод writeData
        #  обёрнутого объекта (wrappee).

    def readData(self):
        data = super().readData()
        return f'{data}'.replace('***','')
        #  1. Получить данные из метода readData обёрнутого
        #  объекта (wrappee).
        #  2. Расшифровать их, если они зашифрованы.
        #  3. Вернуть результат.

class CompressionDecorator(DataSourceDecorator):
    def writeData(self,data):
        data = '|' + data + '|'
        super().writeData(data)
        # 1. Запаковать поданные данные.
        # 2. Передать запакованные данные в метод writeData
        # обёрнутого объекта (wrappee).

    def readData(self):
        data = super().readData()
        return f'{data}'.replace('|','')
        # 1. Получить данные из метода readData обёрнутого
        # объекта (wrappee).
        # 2. Распаковать их, если они запакованы.
        # 3. Вернуть результат.

# Вариант 1. Простой пример сборки и использования декораторов
def dumbUsageExample(salaryRecords, compression:bool, encription:bool):
  source = FileDataSource("somefile.dat")
  if (encription):
    source = EncryptionDecorator(source)
  if (compression):
    source = CompressionDecorator(source)
  source.writeData(salaryRecords)
  return source.readData()
  
print(dumbUsageExample('salaryRecords', True, True))


#  Вариант 2. Клиентский код, использующий внешний источник
#  данных. Класс SalaryManager ничего не знает о том, как именно
#  будут считаны и записаны данные. Он получает уже готовый
#  источник данных.
class SalaryManager:
    def __init__(self,source: DataSource):
      self.source = source
      print('создан менеджер')

    def load(self):
        print('менеджер читает данные')
        return self.source.readData()

    def save(self,salaryRecords):
        self.source.writeData(salaryRecords)
        print('менеджер записал данные')
    
# Приложение может по-разному собирать декорируемые объекты, в
# зависимости от условий использования.

def extendedUsageExample(salaryRecords, compression:bool, encription:bool):
  source = FileDataSource("somefile.dat")
  if (encription):
    source = EncryptionDecorator(source)
  if (compression):
    source = CompressionDecorator(source)
  logger = SalaryManager(source)
  logger.save(salaryRecords)
  return logger.load()

print(extendedUsageExample('salaryRecords', True, True))

import requests as r

class requests:
  '''
  Requests HTTP Library
  Requests is an HTTP library, written in Python, for human beings. Basic GET usage:
  '''
  @staticmethod
  def get(addr):
    '''
    r = requests.get('htts://proxy.com?get=https://www.python.org')
    '''
    print('get '+addr)
    return r.get(addr)
    
print(requests.get('https://ya.ru'))
print(r.get('https://ya.ru'))

class Subject(ABC):
    """
    Интерфейс издателя объявляет набор методов для управлениями подписчиками.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Присоединяет наблюдателя к издателю.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Отсоединяет наблюдателя от издателя.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Уведомляет всех наблюдателей о событии.
        """
        pass


class ConcreteSubject(Subject):
    """
    Издатель владеет некоторым важным состоянием и оповещает наблюдателей о его
    изменениях.
    """

    _state: int = None
    """
    Для удобства в этой переменной хранится состояние Издателя, необходимое всем
    подписчикам.
    """

    _observers: List[Observer] = []
    """
    Список подписчиков. В реальной жизни список подписчиков может храниться в
    более подробном виде (классифицируется по типу события и т.д.)
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    Методы управления подпиской.
    """

    def notify(self) -> None:
        """
        Запуск обновления в каждом подписчике.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Обычно логика подписки – только часть того, что делает Издатель.
        Издатели часто содержат некоторую важную бизнес-логику, которая
        запускает метод уведомления всякий раз, когда должно произойти что-то
        важное (или после этого).
        """

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 4)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    Интерфейс Наблюдателя объявляет метод уведомления, который издатели
    используют для оповещения своих подписчиков.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Получить обновление от субъекта.
        """
        pass


"""
Конкретные Наблюдатели реагируют на обновления, выпущенные Издателем, к которому
они прикреплены.
"""


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
   
   
    
class Command(ABC):
    """
    Интерфейс Команды объявляет метод для выполнения команд.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    """
    Некоторые команды способны выполнять простые операции самостоятельно.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing"
              f"({self._payload})")


class ComplexCommand(Command):
    """
    Но есть и команды, которые делегируют более сложные операции другим
    объектам, называемым «получателями».
    """

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """
        Сложные команды могут принимать один или несколько объектов-получателей
        вместе с любыми данными о контексте через конструктор.
        """

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        Команды могут делегировать выполнение любым методам получателя.
        """

        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    """
    Классы Получателей содержат некую важную бизнес-логику. Они умеют выполнять
    все виды операций, связанных с выполнением запроса. Фактически, любой класс
    может выступать Получателем.
    """

    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")


class Invoker:
    """
    Отправитель связан с одной или несколькими командами. Он отправляет запрос
    команде.
    """

    _on_start = None
    _on_finish = None

    """
    Инициализация команд.
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        Отправитель не зависит от классов конкретных команд и получателей.
        Отправитель передаёт запрос получателю косвенно, выполняя команду.
        """

        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    """
    Клиентский код может параметризовать отправителя любыми командами.
    """

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Send email", "Save report"))

    invoker.do_something_important()
    
    
    
    
class Context():
    """
    Контекст определяет интерфейс, представляющий интерес для клиентов.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Обычно Контекст принимает стратегию через конструктор, а также
        предоставляет сеттер для её изменения во время выполнения.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        Контекст хранит ссылку на один из объектов Стратегии. Контекст не знает
        конкретного класса стратегии. Он должен работать со всеми стратегиями
        через интерфейс Стратегии.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Обычно Контекст позволяет заменить объект Стратегии во время выполнения.
        """

        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
        Вместо того, чтобы самостоятельно реализовывать множественные версии
        алгоритма, Контекст делегирует некоторую работу объекту Стратегии.
        """

        # ...

        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

        # ...


class Strategy(ABC):
    """
    Интерфейс Стратегии объявляет операции, общие для всех поддерживаемых версий
    некоторого алгоритма.

    Контекст использует этот интерфейс для вызова алгоритма, определённого
    Конкретными Стратегиями.
    """

    @abstractmethod
    def do_algorithm(self, data: List):
        pass


"""
Конкретные Стратегии реализуют алгоритм, следуя базовому интерфейсу Стратегии.
Этот интерфейс делает их взаимозаменяемыми в Контексте.
"""


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":
    # Клиентский код выбирает конкретную стратегию и передаёт её в контекст.
    # Клиент должен знать о различиях между стратегиями, чтобы сделать
    # правильный выбор.

    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()
    
    
    
"""
Для создания итератора в Python есть два абстрактных класса из встроенного
модуля collections - Iterable, Iterator. Нужно реализовать метод __iter__() в
итерируемом объекте (списке), а метод __next__() в итераторе.
"""


class AlphabeticalOrderIterator(Iterator):
    """
    Конкретные Итераторы реализуют различные алгоритмы обхода. Эти классы
    постоянно хранят текущее положение обхода.
    """

    """
    Атрибут _position хранит текущее положение обхода. У итератора может быть
    множество других полей для хранения состояния итерации, особенно когда он
    должен работать с определённым типом коллекции.
    """
    _position: int = None

    """
    Этот атрибут указывает направление обхода.
    """
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Any:
        """
        Метод __next __() должен вернуть следующий элемент в последовательности.
        При достижении конца коллекции и в последующих вызовах должно вызываться
        исключение StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    """
    Конкретные Коллекции предоставляют один или несколько методов для получения
    новых экземпляров итератора, совместимых с классом коллекции.
    """

    def __init__(self, collection: list[Any] | None = None) -> None:
        self._collection = collection or []


    def __getitem__(self, index: int) -> Any:
        return self._collection[index]

    def __iter__(self) -> AlphabeticalOrderIterator:
        """
        Метод __iter__() возвращает объект итератора, по умолчанию мы возвращаем
        итератор с сортировкой по возрастанию.
        """
        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self, True)

    def add_item(self, item: Any) -> None:
        self._collection.append(item)


if __name__ == "__main__":
    # Клиентский код может знать или не знать о Конкретном Итераторе или классах
    # Коллекций, в зависимости от уровня косвенности, который вы хотите
    # сохранить в своей программе.
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")
    
# Создайте приложение для работы в библиотеке. Оно
# должно оперировать следующими сущностями: Книга,
# Библиотекарь, Читатель. Приложение должно позволять
# вводить, удалять, изменять, сохранять в файл, загружать из
# файла, логгировать действия, искать информацию (результаты поиска выводятся на экран или файл) о сущностях.
# При реализации используйте максимально возможное
# количество паттернов проектирования.

# Перенесено в модуль
# class SateManager:
#   __instance = None
#   def __new__(cls, *args, **kwargs):
#     if cls.__instance is None:
#       cls.__instance = super().__new__(cls)
#     return cls.__instance
#   def load(self, data):
#     '''
#     data is dict with filename keys 
#     '''
#     for el in data.keys():
#       with open(el+'.pickle', 'rb') as f:
#         data[el].extend(pickle.load(f))
#   def save(self, el:Book|Human, l:Library):
#     name = el.__class__.__name__.lower()
#     with open(name+'s.pickle', 'wb') as f:
#       pickle.dump(l.data[name+'s'], f)

class LibraryApp:
  library:Library
  @staticmethod
  def init():
    LibraryApp.library = Library()
    
  
  
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
    
    
class SourceCodeMixin:
  @property
  def sourcecode(self):
    return inspect.getsource(self.__class__)    
      
class Book(SourceCodeMixin):
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
    
class Human:
  def __init__ (self, name:str, snils:int, year:int):
    self.snils = snils
    self.name = name
    self.year = year

class Librarian(Human):
  pass

class Reader(Human):
  pass  

# LibraryApp.init()
      
b = Book('sdf','sdfsd',1002)
print(b.sourcecode)

def sum(arr):
  return 5  

# assert sum([1, 2, 3]) == 6, "Should be 6"


data = {'a':1, 'b':2}

print({**data})