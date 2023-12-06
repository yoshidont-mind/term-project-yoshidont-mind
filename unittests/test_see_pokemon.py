import io
from unittest import TestCase
from unittest.mock import patch

from battle import see_pokemon


class TestSeePokemon(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_now_in_battle(self, mock_output):
        character = {'Name': 'Red', 'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22,
                                                 'HP': 22, 'Attack': 11, 'Defense': 11, 'Exp to next level': 5,
                                                 'Exp': 0}]}
        my_pokemon = character['Pokemon'][0]
        see_pokemon(character, my_pokemon)
        expected = "Now in battle: Bulbasaur"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_first_pokemon_name(self, mock_output):
        character = {'Name': 'Red', 'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22,
                                                 'HP': 22, 'Attack': 11, 'Defense': 11, 'Exp to next level': 5,
                                                 'Exp': 0}]}
        my_pokemon = character['Pokemon'][0]
        see_pokemon(character, my_pokemon)
        expected = "1) Bulbasaur"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_hp(self, mock_output):
        character = {'Name': 'Red', 'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22,
                                                 'HP': 22, 'Attack': 11, 'Defense': 11, 'Exp to next level': 5,
                                                 'Exp': 0}]}
        my_pokemon = character['Pokemon'][0]
        see_pokemon(character, my_pokemon)
        expected = "HP     : 22 / 22"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_pokemon_name_not_first(self, mock_output):
        character = {'Name': 'Red', 'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22,
                                                 'HP': 22, 'Attack': 11, 'Defense': 11, 'Exp to next level': 5,
                                                 'Exp': 0},
                                                {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22,
                                                 'Attack': 11, 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        my_pokemon = character['Pokemon'][0]
        see_pokemon(character, my_pokemon)
        expected = "2) Squirtle"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
