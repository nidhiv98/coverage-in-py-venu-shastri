import unittest
import string_calculator



  

class String_calculatorTest(unittest.TestCase):
  def given_empty_string_zero_expected(self):
    self.assertTrue(string_calculator.add("0") == 0)
  

if __name__ == '__main__':
  unittest.main()

