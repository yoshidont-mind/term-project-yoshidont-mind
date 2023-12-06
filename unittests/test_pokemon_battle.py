import io
from unittest import TestCase
from unittest.mock import patch

from battle import pokemon_battle


class TestPokemonBattle(TestCase):
    @patch('builtins.input', return_value='1')
    @patch('battle.execute_turn', return_value='lose')
    def test_turn_result_is_lose(self, _, __):
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        trainer_battle = True
        expected = False
        actual = pokemon_battle(character, my_pokemon, foe_pokemon, trainer_battle)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='2')
    @patch('battle.execute_turn', return_value='win')
    def test_turn_result_is_win(self, _, __):
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        trainer_battle = True
        expected = True
        actual = pokemon_battle(character, my_pokemon, foe_pokemon, trainer_battle)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2', '1'])
    @patch('battle.execute_turn', side_effect=['continue', 'win'])
    def test_more_than_one_turn_needed(self, _, __):
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        trainer_battle = True
        expected = True
        actual = pokemon_battle(character, my_pokemon, foe_pokemon, trainer_battle)
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.execute_turn', return_value='lose')
    @patch('builtins.input', side_effect=['Hello World', '2'])
    def test_print_when_user_input_is_invalid_at_first(self, _, __, mock_output):
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        trainer_battle = True
        expected = "\nYou're choice is not valid. Please try it again.\n"
        pokemon_battle(character, my_pokemon, foe_pokemon, trainer_battle)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
