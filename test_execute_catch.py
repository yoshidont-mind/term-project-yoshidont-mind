import io
from unittest import TestCase
from unittest.mock import patch

from battle import execute_catch


class TestExecuteCatch(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_when_character_has_no_poke_balls(self, mock_output):
        character = {'Name': 'Red', 'Item': {'Poke Ball': 0}}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        execute_catch(character, my_pokemon, foe_pokemon)
        actual = mock_output.getvalue()
        expected = "\nYou don't have any Poké Ball!"
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_when_character_has_six_pokemon(self, mock_output):
        character = {'Name': 'Red', 'Item': {'Poke Ball': 1}, 'Pokemon': [{}, {}, {}, {}, {}, {}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        execute_catch(character, my_pokemon, foe_pokemon)
        actual = mock_output.getvalue()
        expected = "\nYou cannot bring more than six Pokémon!"
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.pokemon_catch', return_value=True)
    def test_print_when_catch_success(self, _, mock_output):
        character = {'Name': 'Red', 'Item': {'Poke Ball': 1}, 'Pokemon': [{}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        execute_catch(character, my_pokemon, foe_pokemon)
        actual = mock_output.getvalue()
        expected = "Congratulations! You've caught Squirtle successfully!"
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.pokemon_catch', return_value=False)
    def test_print_when_catch_fail(self, _, mock_output):
        character = {'Name': 'Red', 'Item': {'Poke Ball': 1}, 'Pokemon': [{}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        execute_catch(character, my_pokemon, foe_pokemon)
        actual = mock_output.getvalue()
        expected = "Woops, you failed to catch Squirtle."
        self.assertIn(expected, actual)

    def test_poke_ball_decrease(self):
        character = {'Name': 'Red', 'Item': {'Poke Ball': 1}, 'Pokemon': [{}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        execute_catch(character, my_pokemon, foe_pokemon)
        actual = character['Item']['Poke Ball']
        expected = 0
        self.assertEqual(actual, expected)

    @patch('battle.pokemon_catch', return_value=False)
    def test_turn_result_when_my_pokemon_is_defeated_after_fail_catch(self, _):
        character = {'Name': 'Red', 'Item': {'Poke Ball': 1}, 'Pokemon': [{}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 3, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        actual = execute_catch(character, my_pokemon, foe_pokemon)
        expected = 'lose'
        self.assertEqual(actual, expected)

    @patch('battle.pokemon_catch', return_value=False)
    def test_turn_result_when_catch_fail_and_my_pokemon_is_alive(self, _):
        character = {'Name': 'Red', 'Item': {'Poke Ball': 1}, 'Pokemon': [{}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 10, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 10, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        actual = execute_catch(character, my_pokemon, foe_pokemon)
        expected = 'continue'
        self.assertEqual(actual, expected)

    @patch('battle.pokemon_catch', return_value=True)
    def test_turn_result_when_catch_success(self, _):
        character = {'Name': 'Red', 'Item': {'Poke Ball': 1}, 'Pokemon': [{}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 10, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 10, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        actual = execute_catch(character, my_pokemon, foe_pokemon)
        expected = 'win'
        self.assertEqual(actual, expected)

    def test_turn_result_when_character_has_six_pokemon(self):
        character = {'Name': 'Red', 'Item': {'Poke Ball': 1}, 'Pokemon': [{}, {}, {}, {}, {}, {}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 10, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 10, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        actual = execute_catch(character, my_pokemon, foe_pokemon)
        expected = 'continue'
        self.assertEqual(actual, expected)

    def test_turn_result_when_character_has_no_poke_balls(self):
        character = {'Name': 'Red', 'Item': {'Poke Ball': 0}, 'Pokemon': [{}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 10, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 10, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        actual = execute_catch(character, my_pokemon, foe_pokemon)
        expected = 'continue'
        self.assertEqual(actual, expected)
