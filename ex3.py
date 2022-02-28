import unittest
from main import *

class ex3(unittest.TestCase):


    def test1(self):
        f = lambda x: x
        a = 0
        b = 3
        self.assertTrue(a <= find_root(f,a,b) <= b)

    def test2(self):
        f = lambda x:5*x**2-5*x-7
        a = 1
        b = 3
        self.assertTrue(a <= find_root(f,a,b) <= b)

    def test3(self):
        f = lambda x:x**3+2*x**2-5*x-7
        a = 1
        b = 3
        self.assertTrue(a <= find_root(f,a,b) <= b)

    def test4(self):
        f = lambda x:x**4+x**3+2*x**2-5*x-7
        a = 1
        b = 3
        self.assertTrue(a <= find_root(f,a,b) <= b)

    def test5(self):
        f = lambda x:x**12-x**4+x**3+2*x**2-5*x-7
        a = 1
        b = 3
        self.assertTrue(a <= find_root(f,a,b) <= b)


if __name__ == '__main__':
    unittest.main()