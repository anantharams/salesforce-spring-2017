import unittest
import tests

if not tests.USE_ANSWERS:
    from excercises.functions import power_list_factory, dict_updater_factory, \
        cycle_colors
else:
    from answers.functions import power_list_factory, dict_updater_factory, \
        cycle_colors

class FunctionExcercises(unittest.TestCase):

    def test_cycle_colors(self):
        def g(): yield None 
        generator_type = type(g())
        colors = ['r', 'g', 'b']

        self.assertEqual(type(cycle_colors(colors)), generator_type)

        color_generator = cycle_colors(colors)

        for i in range(100000):
            idx = i % len(colors)
            color = next(color_generator)
            self.assertEqual(colors[idx], color)

    def test_power_list_factory(self):
        func = power_list_factory()
        p = 2
        self.assertEqual(func(p, 0, 1, 2, 3, 4), sum([x**2 for x in range(5)]))
        self.assertEqual(func(10, 0), 0)

    def test_dict_updater_factory(self):
        d1, d2 = {'a' : 1, 'b' : 2}, {'b' : 10, 'c' : 3}
        func = dict_updater_factory()
        self.assertEqual(func(d1, d2), {'a' : 1, 'b' : 10, 'c' : 3})
