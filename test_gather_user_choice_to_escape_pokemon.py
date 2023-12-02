from unittest import TestCase
from unittest.mock import patch

from game import gather_user_choice_to_escape_pokemon


class TestGatherUserChoiceToEscapePokemon(TestCase):
    @patch('builtins.input', side_effect=['2'])
    def test_number_of_pokemon_is_two_and_user_choice_is_valid(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}, {'Name': 'Charmander'}]}
        expect = 2
        actual = gather_user_choice_to_escape_pokemon(character)
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_number_of_pokemon_is_more_than_two_and_user_choice_is_valid(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}, {'Name': 'Charmander'}, {'Name': 'Squirtle'}]}
        expect = 3
        actual = gather_user_choice_to_escape_pokemon(character)
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=['3.4'])
    def test_number_of_pokemon_is_two_and_user_choice_is_invalid(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}, {'Name': 'Charmander'}]}
        expect = 0
        actual = gather_user_choice_to_escape_pokemon(character)
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=['Hello World'])
    def test_number_of_pokemon_is_more_than_two_and_user_choice_is_invalid(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}, {'Name': 'Charmander'}, {'Name': 'Squirtle'}]}
        expect = 0
        actual = gather_user_choice_to_escape_pokemon(character)
        self.assertEqual(expect, actual)
