import io
from unittest import TestCase
from unittest.mock import patch

from battle import execute_both_attacks


class TestExecuteBothAttacks(TestCase):
    def test_foe_pokemon_is_defeated(self):
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 3, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        execute_both_attacks(my_pokemon, foe_pokemon)
        actual = foe_pokemon['HP']
        expected = 0
        self.assertEqual(actual, expected)

    def test_my_pokemon_is_defeated(self):
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 3, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        execute_both_attacks(my_pokemon, foe_pokemon)
        actual = my_pokemon['HP']
        expected = 0
        self.assertEqual(actual, expected)

    def test_both_pokemon_are_alive(self):
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        execute_both_attacks(my_pokemon, foe_pokemon)
        actual = [my_pokemon['HP'], foe_pokemon['HP']]
        expected = [17, 17]
        self.assertEqual(actual, expected)

    def test_turn_result_when_win(self):
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 3, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        actual = execute_both_attacks(my_pokemon, foe_pokemon)
        expected = 'win'
        self.assertEqual(actual, expected)

    def test_turn_result_when_lose(self):
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 3, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        actual = execute_both_attacks(my_pokemon, foe_pokemon)
        expected = 'lose'
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_when_foe_is_defeated(self, mock_output):
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 3, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        execute_both_attacks(my_pokemon, foe_pokemon)
        expected = 'Bulbasaur beat Squirtle!'
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_when_my_pokemon_is_defeated(self, mock_output):
        my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 3, 'Attack': 11,
                      'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                       'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        execute_both_attacks(my_pokemon, foe_pokemon)
        expected = 'Bulbasaur is defeated!\n'
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
