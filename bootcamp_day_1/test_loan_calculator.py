import unittest
from loan_calculator import loancalculator


class Loan_calculator(unittest.TestCase):
    def test_it_works(self):
        self.assertEquals(loancalculator(100000, 12, 10), 110000.0)

    def test_check_month_greater_than_zero(self):
        self.assertEquals(loancalculator(100000, 0.5, 10), 'Invalid month')

    def test_returns_error_msg__if_negative_amount(self):
        self.assertEquals(loancalculator(-100000, 12, 10), 'Invalid amount')

    def test_returns_error_message_if_args_not_numbers(self):
        self.assertRaises(ValueError, loancalculator, 'twenty', 'three', 'ten')

if __name__ == '__main__':
    unittest.main()
