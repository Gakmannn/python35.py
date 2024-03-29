import contextlib

with contextlib.suppress(ImportError):
    from pyscript import window
    input = window.prompt
    print = window.alert

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
    print(f"sum is {total}")
  else:
    print(f"mul is {total}")
    