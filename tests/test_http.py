import unittest
import tests

if not tests.USE_ANSWERS:
    from excercises.http import scrape_channels
else:
    from answers.http import scrape_channels

class HTTPExcercises(unittest.TestCase):
    def test_scrape_channels(self):
        answer = [462.5625, 462.6125, 462.6625, 462.7125, 462.55, 462.6, 462.65, 462.7, 
            462.5875, 462.6375, 462.6875, 467.5625, 467.6125, 467.6625, 467.7125, 462.575, 
            462.625, 462.675, 462.725, 462.5625, 462.6125, 462.6625, 462.7125, 462.55, 462.6, 
            462.65, 462.7, 462.5875]
        self.assertEqual(scrape_channels(), answer)