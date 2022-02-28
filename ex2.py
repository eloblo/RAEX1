import unittest
from main import *

class ex2(unittest.TestCase):

    def test_set(self):
        x = {'5','2','6'}
        self.assertEqual("{'2', '5', '6'}",print_sorted(x))

    def test_list(self):
        x = ['5', '2', '6']
        sorted = ['2', '5', '6']
        self.assertEqual(str(sorted), print_sorted(x))

    def test_tuple(self):
        x = ('5', '2', '6')
        sorted = ('2', '5', '6')
        self.assertEqual(str(sorted), print_sorted(x))

    def test_dict(self):
        x = {'c':2, 'a':5, 'b':66}
        sorted = {'a': 5, 'b': 66, 'c': 2}
        self.assertEqual(str(sorted), print_sorted(x))

    def test_diverse(self):
        x = {'d': 5, 'a': (5, 2, 3), 'b': [[10, 4], [20, 3], [5, 6]]}
        sorted = {'a': (2, 3, 5), 'b': [[3, 20], [4, 10], [5, 6]], 'd': 5}
        self.assertEqual(str(sorted), print_sorted(x))

    def test_unchanged(self):
        x = {'d': 5, 'a': (5, 2, 3), 'b': [[10, 4], [20, 3], [5, 6]]}
        self.assertEqual(str(x), "{'d': 5, 'a': (5, 2, 3), 'b': [[10, 4], [20, 3], [5, 6]]}")


if __name__ == '__main__':
    unittest.main()