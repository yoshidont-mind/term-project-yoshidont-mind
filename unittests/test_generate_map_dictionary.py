from unittest import TestCase
from game import generate_map_dictionary


import unittest


class TestGenerateMapDictionary(unittest.TestCase):
    def test_left_top_corner(self):
        map_dict = generate_map_dictionary()
        self.assertEqual(map_dict[(0, 0)], '▓')

    def test_left_bottom_corner(self):
        map_dict = generate_map_dictionary()
        self.assertEqual(map_dict[(0, 24)], '▓')

    def test_right_top_corner(self):
        map_dict = generate_map_dictionary()
        self.assertEqual(map_dict[(20, 0)], '▓')

    def test_right_bottom_corner(self):
        map_dict = generate_map_dictionary()
        self.assertEqual(map_dict[(20, 24)], '▓')

    def test_left_wall(self):
        map_dict = generate_map_dictionary()
        self.assertEqual(map_dict[(0, 10)], '▓')

    def test_right_wall(self):
        map_dict = generate_map_dictionary()
        self.assertEqual(map_dict[(20, 10)], '▓')

    def test_top_wall(self):
        map_dict = generate_map_dictionary()
        self.assertEqual(map_dict[(10, 0)], '▓')

    def test_bottom_wall(self):
        map_dict = generate_map_dictionary()
        self.assertEqual(map_dict[(10, 24)], '▓')

    def test_middle(self):
        map_dict = generate_map_dictionary()
        self.assertEqual(map_dict[(12, 10)], '@')
