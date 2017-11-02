import unittest
from metmap.metmap import do_it_all


class TestMetMap(unittest.TestCase):
    def test_main_function(self):
        self.assertEqual(len(do_it_all("test_data.txt")), 1)
