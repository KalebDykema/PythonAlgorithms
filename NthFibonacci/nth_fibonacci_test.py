import unittest
from nth_fibonacci_solution import getNthFib

class TestAlgo(unittest.TestCase):
   def test_case_1(self):
      self.assertEqual(getNthFib(6), 5)
   
   def test_case_2(self):
      self.assertEqual(getNthFib(1), 0)
   
   def test_case_3(self):
      self.assertEqual(getNthFib(2), 1)
   
   def test_case_4(self):
      self.assertEqual(getNthFib(2), 1)
   
   def test_case_5(self):
      self.assertEqual(getNthFib(2), 1)

if __name__ == "__main__":
   unittest.main()