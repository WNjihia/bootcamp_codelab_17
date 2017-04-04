import unittest
from oop import *


class oopTest(unittest.TestCase):

    def test_person_instance(self):
        tenant1 = Tenant('Sue', 'Jackson', 10000)
        owner1 = Property_owner('Ian', 'Smith', [tenant1])
        self.assertIsInstance(owner1, Person, msg='The object should be an instance of the `Person` class')

if __name__ == '__main__':
    unittest.main()
