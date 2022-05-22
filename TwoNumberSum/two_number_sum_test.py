import unittest
from two_number_sum_solution import twoNumberSum

class TestAlgo(unittest.TestCase):
   def test_case_1(self):
      output = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
      self.assertTrue(len(output) == 2)
      self.assertTrue(11 in output)
      self.assertTrue(-1 in output)
   
   def test_case_2(self):
      output = twoNumberSum([4, 6], 10)
      self.assertTrue(len(output) == 2)
      self.assertTrue(4 in output)
      self.assertTrue(6 in output)
   
   def test_case_3(self):
      output = twoNumberSum([4, 6, 1], 5)
      self.assertTrue(len(output) == 2)
      self.assertTrue(4 in output)
      self.assertTrue(1 in output)
   
   def test_case_4(self):
      output = twoNumberSum([4, 6, 1, -3], 3)
      self.assertTrue(len(output) == 2)
      self.assertTrue(6 in output)
      self.assertTrue(-3 in output)
   
   def test_case_5(self):
      output = twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 17)
      self.assertTrue(len(output) == 2)
      self.assertTrue(8 in output)
      self.assertTrue(9 in output)
   
   def test_case_6(self):
      output = twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18)
      self.assertTrue(len(output) == 2)
      self.assertTrue(3 in output)
      self.assertTrue(15 in output)
   
   def test_case_7(self):
      output = twoNumberSum([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5)
      self.assertTrue(len(output) == 2)
      self.assertTrue(-5 in output)
      self.assertTrue(0 in output)
   
   def test_case_8(self):
      output = twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163)
      self.assertTrue(len(output) == 2)
      self.assertTrue(210 in output)
      self.assertTrue(-47 in output)
   
   def test_case_9(self):
      output = twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164)
      self.assertTrue(len(output) == 0)
   
   def test_case_10(self):
      output = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 15)
      self.assertTrue(len(output) == 0)
   
   def test_case_11(self):
      output = twoNumberSum([14], 15)
      self.assertTrue(len(output) == 0)
   
   def test_case_12(self):
      output = twoNumberSum([15], 15)
      self.assertTrue(len(output) == 0)

if __name__ == "__main__":
   unittest.main()