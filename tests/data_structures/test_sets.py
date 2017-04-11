import unittest
import tests

if not tests.USE_ANSWERS:
    from excercises.data_structures.set_excercises import similar, \
        contained, copy_and_change_set
else:
    from answers.data_structures.set_excercises import similar, \
        contained, copy_and_change_set

class SetExcercises(unittest.TestCase):
    
    def test_similar(self):
        self.assertEqual(similar(['a', 'b'], ['b']), ['b'])
        self.assertEqual(similar([], []), [])
        self.assertEqual(similar(['b'], []), [])
        self.assertEqual(similar(['b', 'b', 'b', 'e'], ['b', 'd', 'z']), ['b'])

    def test_contained(self):
        big = set(list('abcdefgh'))
        small = set(list('abcd'))
        smaller = set()
        self.assertEqual(contained(big, small), True)
        self.assertEqual(contained(small, big), False)
        self.assertEqual(contained(big, small), True)
        self.assertEqual(contained(big, smaller), True)
        self.assertEqual(contained(small, smaller), True)

    def test_copy_and_change_set(self):
        original = set(range(10))
        item = 'apple'
        new_set = set(original)
        new_set.add(item)

        self.assertEqual(copy_and_change_set(original, item), new_set)
