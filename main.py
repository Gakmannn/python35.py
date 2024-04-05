import contextlib

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