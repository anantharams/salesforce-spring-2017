import unittest
import tests

if not tests.USE_ANSWERS:
    from excercises.data_structures.tuple_excercises import filter_and_rank_teams
else:
    from answers.data_structures.tuple_excercises import filter_and_rank_teams

class TupleExcercises(unittest.TestCase):
    """
    $ py.test tests/test_ds.py::TupleExcercises
    """
    def test_filter_and_rank_teams(self):
        items = [
            (8, "Seahawks"), 
            (11, "49ers"), 
            (12, "Green Bay"),
            (9, "Packers"), 
            (13, "Patriots"),
            (12, "Jets"),
        ]
        right_items = [ 
            (13, "Patriots"),
            (12, "Jets"), 
            (11, "49ers"),
        ]
        self.assertEqual(filter_and_rank_teams(items, 11, ["Green Bay"], 3), right_items)
