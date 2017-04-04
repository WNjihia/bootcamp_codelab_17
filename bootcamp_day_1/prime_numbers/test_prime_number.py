import unittest
from prime_number import gen_prime_number


class Generate_prime_numbers(unittest.TestCase):
    def test_it_works(self):
        self.assertEquals(gen_prime_number(10), [2, 3, 5, 7])

    def test_returns_error_msg_if_value_is_negative(self):
        self.assertEquals(gen_prime_number(-10), 'Invalid input')

    def test_returns_error_msg_if_value_is_zero(self):
        self.assertEquals(gen_prime_number(0), 'Invalid input')

if __name__ == '__main__':
    unittest.main()
