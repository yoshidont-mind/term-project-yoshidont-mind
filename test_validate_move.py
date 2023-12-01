from unittest import TestCase

from game import validate_move, generate_map_dictionary


class TestValidateMove(TestCase):
    def test_valid_move(self):
        map_dic = generate_map_dictionary()
        character = {'Location': [15, 1]}
        direction = '4'
        expected = True
        self.assertEqual(expected, validate_move(map_dic, character, direction))

    def test_new_location_is_out_of_bounds(self):
        map_dic = generate_map_dictionary()
        character = {'Location': [0, 0]}
        direction = '1'
        expected = False
        self.assertEqual(expected, validate_move(map_dic, character, direction))

    def test_new_location_is_obstacle(self):
        map_dic = generate_map_dictionary()
        character = {'Location': [15, 1]}
        direction = '3'
        expected = False
        self.assertEqual(expected, validate_move(map_dic, character, direction))
