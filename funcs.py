import contextlib
import string
import random
# node makehtml.js

with contextlib.suppress(ImportError):
  from pyscript import window
  input = window.prompt
  print = window.alert


def DZ_2_1_1_SumOrMul(event):
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит 
# на экран сумму трёх чисел или произведение трёх чисел
  numsStr = input('3 num split space')
  nums=''
  if numsStr:
    nums = numsStr.split()
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
    print(f"sum is {total}")
  else:
    print(f"mul is {total}")
    
    
def DZ_3_2_4_min_max_sum(event):
# Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум, 
# введенных чисел. Когда пользователь вводит число 7 
# программа прекращает свою работу и выводит на экран 
# надпись «Good bye!»
  sum = 0
  min = None
  max = None
  while True:
    n = input('Введите число')
    if n:
      n = int(n)
    else:
      return
    if n==7:
      print('Good bye')
      break
    if min==None and max==None:
      min = n
      max = n
    if n>max:
      max = n
    if n<min:
      min = n
    sum+=n
    print(f"min = {min}\nmax = {max}\nsum = {sum}")
    
def DZ_3_3_4_remove3and6(event):
# Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все цифры 3 и 6 и 
# вывести обратно на экран. 
  n = input('Введите число')
  if n:
    n = int(n)
  else:
    return
  # print (''.join(''.join(nStr.split('3')).split('6')))
  tail = ''
  while n:
    if not (n%10==3 or n%10==6):
      tail = str(n%10) + tail
    n//=10
  print(tail)

def DZ_4_1_2_strings_replace(event):
# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст.
  text = input('Введите текст')
  words = input('Введите список зарезервированных слов через пробел').split()
  for word in words:
     text = text.replace(word, word.upper())
  print(text)    

def DZ_3_5_1_print_figure(event):
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
  
def DZ_10_1_3_print_square(event):
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
  
  l = int(input('Введите сторону квадрата'))
  s = input('Введите символ')
  z = bool(int(input('Закрашивать? (0,1)')))
  printSquere(l, s, z)  
  
def DZ_5_3_5_bulls_and_cows(event):
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
  # print(num)
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

def print_square(event):
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
  
  l = int(input('Введите сторону квадрата'))
  s = input('Введите символ')
  z = bool(int(input('Закрашивать? (0,1)')))
  printSquere(l, s, z)  
  
def PZ_10_3_5_bulls_and_cows(event):
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
  # print(num)
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

def bulls_and_cows(event):
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
  # print(num)
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
  