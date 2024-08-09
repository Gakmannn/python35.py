# Создайте класс, содержащий набор целых чисел.
# ■ Сумма элементов набора.
# ■ Среднеарифметическое элементов набора.
# ■ Максимум из элементов набора.
# ■ Минимум из элементов набора.
# Протестируйте все возможности созданного класса
# с помощью модульного тестирования(unittest). 

import unittest
from fractions import Fraction

class IntKit:
  def __init__(self, *args):
    self.list = []
    for el in args:
      if isinstance(el, int) and not isinstance(el, bool):
        self.list.append(el)
  def sum(self):
    return sum(self.list)
  def mid(self):
    return sum(self.list)/len(self.list)
  def max(self):
    return max(self.list)
  def min(self):
    return min(self.list)
  
class TestSum(unittest.TestCase):
  def test_list1(self):
    kit = IntKit(1,.2,3,.5,6,'dsfsfd', False, True, [], {})
    self.assertEqual(kit.sum(), 10, "Should be 10")
    self.assertEqual(kit.mid(), 10/3, "Should be 10/3")
    self.assertEqual(kit.max(), 6, "Should be 6")
    self.assertEqual(kit.min(), 1, "Should be 1")
  def test_list2(self):
    kit = IntKit(1,.2,-3,.5,6,'dsfsfd', False, True, [], {})
    self.assertEqual(kit.sum(), 4, "Should be 4")
    self.assertEqual(kit.mid(), 4/3, "Should be 4/3")
    self.assertEqual(kit.max(), 6, "Should be 6")
    self.assertEqual(kit.min(), -3, "Should be -3")

if __name__ == "__main__":
    unittest.main()
