import unittest as ut
import roman_numbers


def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

class TestFibonacci(ut.TestCase):
    # all the tests within this class need to start with test so the test runner knows what to call
    def testFib(self):
        self.assertEqual(fibonacci(10),55)

class TestRoman_numbers(ut.TestCase):
    # all the tests within this class need to start with test so the test runner knows what to call
    def testRoman(self):
        self.assertEqual(roman_numbers.int_to_Roman(145),'CXLV')
    def testRoman(self):
        self.assertEqual(roman_numbers.roman_number(1342),'MCCCXLII')


if __name__ == '__main__':
  ut.main()
