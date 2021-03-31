import unittest
from app import random_function

class Testfunction(unittest.TestCase):
    def test_result(self):
        self.assertAlmostEqual( random_function(2, 3), 6)
        self.assertAlmostEqual( random_function(3, 3), 9)
        self.assertAlmostEqual( random_function(1, 3), 3)