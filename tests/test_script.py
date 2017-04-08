import unittest
import os
from subprocess import check_output

import tests

if not tests.USE_ANSWERS:
    path = os.path.join('excercises', 'script.py')
else:
    path = os.path.join('answers', 'script.py')


class ScriptingExcercises(unittest.TestCase):

    def test_frequency_scraping_script(self):
        # test mean 
        output = float(check_output(['python', path, '--statistic', 'mean']).strip())
        self.assertEqual(output - 463.348214286 < 1e-8, True)

        # test median
        output = float(check_output(['python', path, '--statistic', 'median']).strip())
        self.assertEqual(output - 462.65 < 1e-8, True)

        # test mean
        output = float(check_output(['python', path, '--statistic', 'mean', '--odds']).strip())
        self.assertEqual(output - 463.339285714 < 1e-8, True)

        # test median
        output = float(check_output(['python', path, '--statistic', 'mean', '--evens']).strip())
        self.assertEqual(output - 463.357142857 < 1e-8, True)
