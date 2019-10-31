#TestEmpl.py

import unittest
import MyEmpl # name of py script to test

class myValues(unittest.TestCase):

    @classmethod
    def setUpClass(cls): # runs once before all tests
        print("This is setUpClass.")

    @classmethod
    def tearDownClass(cls): # runs once after all tests
        print("This is tearDownClass.")

    def setUp(self): # runs before every test function
        print("This is setUp.")
        self.emp_1 = MyEmpl.Employee('Walt', 'Disney', "786")
       # self.emp_2 = Employee('Leo', 'Messi', 60000)

    def tearDown(self): # runs after every test function
        print("This is tearDown.")

    def test_set_firstname(self):
        print("This is test_firstname.")
        expected = 'Walt'
        result = self.emp_1.get_firstname()
        self.assertEqual(result, expected)

    def test_set_lastname(self):
        print("This is test_lastname.")
        expected = "Disney"
        result = self.emp_1.get_lastname()
        self.assertEqual(result, expected)

    def test_set_telno(self):
        print("This is test_set_telno.")
        expected = "786"
        result = self.emp_1.get_telno()
        self.assertEqual(result, expected)

    def test_display_all(self):
        pass

if __name__ == '__main__':
    unittest.main()
