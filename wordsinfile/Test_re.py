#Test_re.py

import unittest
import regexp5

class KnownValues(unittest.TestCase):

    @classmethod
    def setUpClass(cls): # runs once before all tests
        print("***setUpClass***")

    @classmethod
    def tearDownClass(cls): # runs once after all tests
        print("***tearDownClass***")

    def setUp(self): # runs before every test function
        print("**setUp**")
        f = open("text.txt")
        f.seek(0)
        self.data1 = f.read()
        f.close()
        g = open("names.txt")
        g.seek(0)
        self.data2 = g.read()
        g.close()

    def tearDown(self): # runs after every test function
        print("**tearDown**")

    def test_find_num11(self):
        print("**test_find_num11**")
        x = regexp5.find_num(self.data1, "people")
        self.assertEqual(2, x)

    def test_find_num12(self):
        print("**test_find_num12**")
        x = regexp5.find_num(self.data1, "the")
        self.assertEqual(14, x)

    def test_find_num21(self):
        print("**test_find_num21**")
        x = regexp5.find_num(self.data2, "Mark")
        self.assertEqual(1, x)

    def test_find_num22(self):
        print("**test_find_num22**")
        x = regexp5.find_num(self.data2, "David")
        self.assertEqual(2, x)

        

if __name__ == '__main__':
    unittest.main()
                         
