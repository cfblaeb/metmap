import unittest
from metmap.metmap import generate_parts_for_cassette


class TestMetMap(unittest.TestCase):
    def test_gpfc(self):
        infile = open("test_data.txt")
        motifs = generate_parts_for_cassette(infile)
        self.assertEqual(104, len(motifs))
        infile.close()

