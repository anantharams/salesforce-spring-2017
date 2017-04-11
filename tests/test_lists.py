import unittest
import tests

if not tests.USE_ANSWERS:
    from excercises.data_structures.list_excercises import evens, csv_line, combine_lists
else:
    from answers.data_structures.list_excercises import evens, csv_line, combine_lists

class ListExcercises(unittest.TestCase):
    """
    $ py.test tests/test_ds.py::ListExcercises
    """
    def test_evens(self):
        self.assertEqual(evens(10), [2, 4, 6, 8, 10])
        self.assertEqual(evens(11), [2, 4, 6, 8, 10])
        self.assertEqual(evens(-1), [])
        self.assertEqual(evens(0), [])
        self.assertEqual(evens(1), [])
        self.assertEqual(evens(2), [2])

    def test_csv_line(self):
        self.assertEqual(csv_line([0, None, 'apple'], ","), "0,None,apple")
        self.assertEqual(csv_line([], ","), "")
        self.assertEqual(csv_line(["Red", "Blue"], "||"), "Red||Blue")

    def test_combine_lists(self):
        l1 = [1, 2, 3]
        l2 = ['a', 'a']
        l3 = ['r', 1]
        self.assertEqual(combine_lists(l1, l2, l3), l1 + l2 + l3)
        self.assertEqual(combine_lists(l1, l1, l1), l1 + l1 + l1)
        self.assertEqual(combine_lists([], [], []), [])

