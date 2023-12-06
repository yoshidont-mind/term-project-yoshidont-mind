import io
from unittest import TestCase
from unittest.mock import patch

from battle import execute_run


class TestExecuteRun(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.run_success', return_value=True)
    def test_print_when_run_success(self, _, mock_output):
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Charmander', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        execute_run(my_pokemon, foe_pokemon)
        expected = "\nYou've successfully run away from Charmander!\n"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('battle.run_success', return_value=True)
    def test_turn_result_when_run_success(self, _):
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Charmander', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        actual = execute_run(my_pokemon, foe_pokemon)
        expected = "win"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.run_success', return_value=False)
    def test_print_when_run_fail(self, _, mock_output):
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Charmander', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        execute_run(my_pokemon, foe_pokemon)
        expected = "\nWoops, you failed to run from Charmander."
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('battle.run_success', return_value=False)
    def test_turn_result_when_run_fail_and_my_pokemon_is_defeated(self, _):
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 2, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Charmander', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        actual = execute_run(my_pokemon, foe_pokemon)
        expected = "lose"
        self.assertEqual(expected, actual)

    @patch('battle.run_success', return_value=False)
    def test_turn_result_when_run_fail_and_my_pokemon_is_not_defeated(self, _):
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Charmander', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        actual = execute_run(my_pokemon, foe_pokemon)
        expected = "continue"
        self.assertEqual(expected, actual)
