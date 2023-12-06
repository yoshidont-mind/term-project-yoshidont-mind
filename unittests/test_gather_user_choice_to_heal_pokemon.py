from unittest import TestCase
from unittest.mock import patch

from game import gather_user_choice_to_heal_pokemon


class TestGatherUserChoiceToHealPokemon(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_number_of_pokemon_is_one_and_user_choice_is_valid(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Squirtle', 'Level': 5, 'HP': 21, 'Max HP': 21}]}
        expect = 1
        actual = gather_user_choice_to_heal_pokemon(character)
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_number_of_pokemon_is_more_than_one_and_user_choice_is_valid(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu', 'Level': 5, 'HP': 21, 'Max HP': 21},
                                                {'Name': 'Charmander', 'Level': 5, 'HP': 21, 'Max HP': 21},
                                                {'Name': 'Squirtle', 'Level': 5, 'HP': 21, 'Max HP': 21}]}
        expect = 3
        actual = gather_user_choice_to_heal_pokemon(character)
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=['3.4'])
    def test_number_of_pokemon_is_one_and_user_choice_is_invalid(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Squirtle', 'Level': 5, 'HP': 21, 'Max HP': 21}]}
        expect = 0
        actual = gather_user_choice_to_heal_pokemon(character)
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=['Hello World'])
    def test_number_of_pokemon_is_more_than_one_and_user_choice_is_invalid(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu', 'Level': 5, 'HP': 21, 'Max HP': 21},
                                                {'Name': 'Charmander', 'Level': 5, 'HP': 21, 'Max HP': 21},
                                                {'Name': 'Squirtle', 'Level': 5, 'HP': 21, 'Max HP': 21}]}
        expect = 0
        actual = gather_user_choice_to_heal_pokemon(character)
        self.assertEqual(expect, actual)
