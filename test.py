import multiprocessing
import time, random
from queue import Empty
from math import factorial
import pickle

def worker(input, output):
    """Функция, выполняемая рабочими процессами"""
    for num in iter(input.get, 'STOP'):
        output.put(is_prime(num))
      
def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a    
    
TASKS = [random.randint(1000,10000) for i in range(0, 1_0000)]

def classic():
  result = []
  for num in TASKS:
    result.append(is_prime(num))
  print(len(result))

def m_q():
    NUMBER_OF_PROCESSES = multiprocessing.cpu_count()
    
    # reverse
    
    # Создание очередей
    task_queue = multiprocessing.Queue()
    done_queue = multiprocessing.Queue()

    results = []
    # Заполнение очереди заданий

    p_list:list[multiprocessing.Process] = []
    
    # Запуск рабочих процессов
    for _ in range(NUMBER_OF_PROCESSES):
      p = multiprocessing.Process(target=worker, args=(task_queue, done_queue))
      p_list.append(p)
      p.start()
    
    i=0
    
    while len(TASKS):    
      if task_queue.empty():
        task_queue.put(TASKS.pop())
        i+=1
      # time.sleep(.000001)
      if i==90:
        i=0
      while not done_queue.empty():
        results.append(done_queue.get(False)) 
    
    for p in p_list:
      task_queue.put('STOP')
    
    for p in p_list:
      p.join()
    
    while not done_queue.empty():
      results.append(done_queue.get(False)) 
    
    print(len(results))
    
  
if __name__ == '__main__':
  # with open('tasks.bin', 'rb') as f:
  #   TASKS = pickle.load(f)
  start = time.perf_counter()
  classic()
  print(time.perf_counter()-start)
  start = time.perf_counter()
  m_q()
  print(time.perf_counter()-start)