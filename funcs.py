import contextlib

with contextlib.suppress(ImportError):
  from pyscript import window
  input = window.prompt
  print = window.alert


def SumOrMul(event):
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
    
    
def DZ3_4_min_max_sum(event):
  sum = 0
  min = None
  max = None
  while True:
    n = int(input('Введите число'))
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
    
def DZ3_3_36(event):
  n = int(input('Введите число'))
  # print (''.join(''.join(nStr.split('3')).split('6')))
  tail = ''
  while n:
    if not (n%10==3 or n%10==6):
      tail = str(n%10) + tail
    n//=10
  print(tail)
    
