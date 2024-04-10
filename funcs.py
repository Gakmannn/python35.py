import contextlib
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
    
    
def DZ3_2_4_min_max_sum(event):
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
    
def DZ3_3_4_remove3and6(event):
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

def DZ4_1_2_strings_replace(event):
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
