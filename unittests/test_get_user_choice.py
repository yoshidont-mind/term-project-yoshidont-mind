from unittest import TestCase
from unittest.mock import patch

from game import get_user_choice
from game import generate_map_dictionary


class TestGetUserChoice(TestCase):
    @patch('builtins.input', return_value='1')
    def test_valid_default_choice(self, _):
        character = {'Name': 'Ash', 'Pokemon': [], 'Location': (15, 1)}
        map_dic = generate_map_dictionary()
        expected = '1'
        actual = get_user_choice(map_dic, character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='7')
    def test_seven_when_valid(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}], 'Location': (15, 1)}
        map_dic = generate_map_dictionary()
        expected = '7'
        actual = get_user_choice(map_dic, character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['7', '1'])
    def test_seven_at_first_when_invalid(self, _):
        character = {'Name': 'Ash', 'Pokemon': [], 'Location': (15, 1)}
        map_dic = generate_map_dictionary()
        expected = '1'
        actual = get_user_choice(map_dic, character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='8')
    def test_eight_or_nine_when_valid(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}, {'Name': 'Charmander'}], 'Location': (15, 1)}
        map_dic = generate_map_dictionary()
        expected = '8'
        actual = get_user_choice(map_dic, character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['8', '1'])
    def test_eight_or_nine_at_first_when_invalid(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}], 'Location': (15, 1)}
        map_dic = generate_map_dictionary()
        expected = '1'
        actual = get_user_choice(map_dic, character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='0')
    def test_zero(self, _):
        character = {'Name': 'Ash', 'Pokemon': [], 'Location': (15, 1)}
        map_dic = generate_map_dictionary()
        expected = '0'
        actual = get_user_choice(map_dic, character)
        self.assertEqual(expected, actual)
