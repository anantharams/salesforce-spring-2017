import unittest
import tests

if not tests.USE_ANSWERS:
    from excercises.data_structures.set_excercises import similar
else:
    from answers.data_structures.set_excercises import similar

class SetExcercises(unittest.TestCase):
    """
    $ py.test tests/test_ds.py::SetExcercises
    """
    def test_similar(self):
        self.assertEqual(similar(['a', 'b'], ['b']), ['b'])
        self.assertEqual(similar([], []), [])
        self.assertEqual(similar(['b'], []), [])
        self.assertEqual(similar(['b', 'b', 'b', 'e'], ['b', 'd', 'z']), ['b'])
