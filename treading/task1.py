# При старте приложения запускаются три потока.
# Первый поток заполняет список случайными числами.
# Два других потока ожидают заполнения. Когда список
# заполнен оба потока запускаются. Первый поток находит
# сумму элементов списка, второй поток среднеарифметическое значение в списке. Полученный список, сумма и
# среднеарифметическое выводятся на экран. 

import threading
from random import randint

list = []
results = {}

def fill(list):
  for _ in range(100000000):
    list.append(randint(0,100))
  print('массив готов')
  # print(list)
  
def mySum(list):
  results['sum']=sum(list)
  # print (sum(list))
  
def mid(list):
  results['mid']=sum(list)/len(list)
  # print (sum(list)/len(list))
  
if __name__ == '__main__':
    t1 = threading.Thread(target=fill, args=(list,), daemon=True)
    t2 = threading.Thread(target=mySum, args=(list,), daemon=True)
    t3 = threading.Thread(target=mid, args=(list,), daemon=True)
    
    t1.start()
    t1.join()
    
    t2.start()
    t3.start()
    t2.join()
    t3.join()
    
    print(results)