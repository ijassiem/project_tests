####TestArea.py#####

import unittest
import MathFunctions
import math

class KnownValues(unittest.TestCase):

    @classmethod
    def setUpClass(cls): # runs once before all tests
        print("This is setUpClass.")

    @classmethod
    def tearDownClass(cls): # runs once after all tests
        print("This is tearDownClass.")

    def setUp(self): # runs before every test function
        print("This is setUp.")

    def tearDown(self): # runs after every test function
        print("This is tearDown.")

    def test_areaCirle_10(self):
        print("This is test_areaCirle.")
        x = 10
        result = MathFunctions.areaCircle(x)
        expected = math.pi*(x)**2
        self.assertEqual(expected, result)

    def test_areaSquare_10(self):
        print("This is test_areasquare_10.")
        x = 10
        result = MathFunctions.areaSquare(x)
        expected = x*x
        self.assertEqual(expected, result)

    def test_areaCirle_fraction(self):
        print("This is test_areaCirle_fraction.")
        x = 1/2
        result = MathFunctions.areaCircle(x)
        expected = math.pi*(x)**2
        self.assertEqual(expected, result)

    def test_areaSquare_fraction(self):
        print("This is test_areaSquare_fraction.")
        x = 10.1
        result = MathFunctions.areaSquare(x)
        expected = x*x
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
    
    ######################
                         
