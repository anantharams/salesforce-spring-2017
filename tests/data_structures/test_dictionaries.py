import unittest
import tests

if not tests.USE_ANSWERS:
    from excercises.data_structures.dictionary_excercises import counter
else:
    from answers.data_structures.dictionary_excercises import counter

class DictExcercises(unittest.TestCase):
    """
    $ py.test tests/test_ds.py::DictExcercises
    """
    def test_counter(self):
        elements = ['a', 'b', 'a', 'c', 's', 's', 's']
        self.assertEqual(counter(elements), {
            'a' : 2, 'b' : 1, 's' : 3, 'c' : 1})
        self.assertEqual(counter([]), {})
        self.assertEqual(counter([None]), {None : 1})
