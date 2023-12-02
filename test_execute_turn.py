import io
from unittest import TestCase
from unittest.mock import patch

from battle import execute_turn


class TestExecuteTurn(TestCase):
    @patch('battle.execute_both_attacks', return_value='execute_both_attacks_is_invoked')
    def test_execute_both_attacks_is_invoked_when_user_input_is_one(self, _):
        user_input = '1'
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        trainer_battle = True
        expected = 'execute_both_attacks_is_invoked'
        actual = execute_turn(user_input, character, my_pokemon, foe_pokemon, trainer_battle)
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_see_pokemon_is_invoked_when_user_input_is_two(self, mock_output):
        user_input = '2'
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        trainer_battle = True
        execute_turn(user_input, character, my_pokemon, foe_pokemon, trainer_battle)
        actual = mock_output.getvalue()
        expected = "Now in battle: Bulbasaur"
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_when_user_input_is_three_and_trainer_battle_is_true(self, mock_output):
        user_input = '3'
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        trainer_battle = True
        expected = '\nYou cannot catch a pokemon in battle with a trainer!\n'
        execute_turn(user_input, character, my_pokemon, foe_pokemon, trainer_battle)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('battle.execute_catch', return_value='execute_catch_is_invoked')
    def test_catch_pokemon_is_invoked_when_user_input_is_three_and_trainer_battle_is_false(self, _):
        user_input = '3'
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        trainer_battle = False
        expected = 'execute_catch_is_invoked'
        actual = execute_turn(user_input, character, my_pokemon, foe_pokemon, trainer_battle)
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_when_user_input_is_four_and_trainer_battle_is_true(self, mock_output):
        user_input = '4'
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        trainer_battle = True
        expected = '\nYou cannot run away from a trainer!\n'
        execute_turn(user_input, character, my_pokemon, foe_pokemon, trainer_battle)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('battle.execute_run', return_value='execute_run_is_invoked')
    def test_execute_run_is_invoked_when_user_input_is_four_and_trainer_battle_is_false(self, _):
        user_input = '4'
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        trainer_battle = False
        expected = 'execute_run_is_invoked'
        actual = execute_turn(user_input, character, my_pokemon, foe_pokemon, trainer_battle)
        self.assertEqual(expected, actual)
