import unittest

def add(number):
  case1=check_empty(number)
  return case1
  
def check_empty(number):  
  if len(number)==0:
    return 0
  
class String_calculatorTest(unittest.TestCase):
  def given_empty_string_zero_expected(self):
    self.assertTrue(add("") == 0)
  

if __name__ == '__main__':
  unittest.main()


  
