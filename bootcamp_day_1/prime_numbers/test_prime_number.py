import unittest
from prime_number import gen_prime_number


class Generate_prime_numbers(unittest.TestCase):
    def test_it_works(self):
        self.assertEquals(gen_prime_number(10), [2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()
