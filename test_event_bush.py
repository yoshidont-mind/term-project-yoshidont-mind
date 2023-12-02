import io
from unittest import TestCase
from unittest.mock import patch

from event import event_bush


class TestEventBush(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('event.check_for_wild_pokemon', return_value=False)
    def test_wild_pokemon_not_appeared(self, _, mock_output):
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        event_bush(character)
        expected = ''
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('event.check_for_wild_pokemon', return_value=True)
    @patch('random.randint', return_value=2)
    @patch('builtins.input', return_value='1')
    @patch('battle.pokemon_battle', return_value=True)
    def test_print_when_wild_pokemon_appeared(self, _, __, ___, ____, mock_output):
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}],
                     'Item': {'Potion': 0, 'Poke Ball': 0},
                     'Trainer rank': 1}
        event_bush(character)
        expected = 'Wild Charmander (Lv. 2) appeared!'
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('event.check_for_wild_pokemon', return_value=True)
    @patch('random.randint', return_value=2)
    @patch('builtins.input', return_value='1')
    @patch('battle.pokemon_battle', return_value=True)
    def test_print_when_wild_pokemon_wins(self, _, __, ___, ____, mock_output):
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}],
                     'Item': {'Potion': 0, 'Poke Ball': 0},
                     'Trainer rank': 1}
        event_bush(character)
        expected = 'Press Enter to continue.\n'
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('event.check_for_wild_pokemon', return_value=True)
    @patch('random.randint', return_value=2)
    @patch('builtins.input', return_value='1')
    @patch('battle.check_alive_pokemon_remains', return_value=False)
    @patch('battle.pokemon_battle', return_value=False)
    def test_print_when_wild_pokemon_wins(self, _, __, ___, ____, _____, mock_output):
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}],
                     'Item': {'Potion': 0, 'Poke Ball': 0},
                     'Trainer rank': 1}
        event_bush(character)
        expected = '\nAll of your Pokémon are defeated!\n'
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
