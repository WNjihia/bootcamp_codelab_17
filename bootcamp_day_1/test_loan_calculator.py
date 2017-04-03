import unittest
from loan_calculator import loancalculator


class Loan_calculator(unittest.TestCase):
    def test_it_works(self):
        self.assertEquals(loancalculator(100000, 12, 10), 110000.0)

if __name__ == '__main__':
    unittest.main()
