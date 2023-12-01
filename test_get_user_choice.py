from unittest import TestCase
from unittest.mock import patch

from game import get_user_choice


class TestGetUserChoice(TestCase):
    @patch('builtins.input', return_value='1')
    def test_valid_default_choice(self, _):
        character = {'Name': 'Ash', 'Pokemon': []}
        expected = '1'
        actual = get_user_choice(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='7')
    def test_seven_when_valid(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}]}
        expected = '7'
        actual = get_user_choice(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['7', '1'])
    def test_seven_at_first_when_invalid(self, _):
        character = {'Name': 'Ash', 'Pokemon': []}
        expected = '1'
        actual = get_user_choice(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='8')
    def test_eight_or_nine_when_valid(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}, {'Name': 'Charmander'}]}
        expected = '8'
        actual = get_user_choice(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['8', '1'])
    def test_eight_or_nine_at_first_when_invalid(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}]}
        expected = '1'
        actual = get_user_choice(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='0')
    def test_zero(self, _):
        character = {'Name': 'Ash', 'Pokemon': []}
        expected = '0'
        actual = get_user_choice(character)
        self.assertEqual(expected, actual)
