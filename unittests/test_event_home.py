import io
from unittest import TestCase
from unittest.mock import patch

from event import event_home


class TestEventHome(TestCase):
    @patch('builtins.input', return_value='')
    def test_pokemon_are_healed(self, _):
        character = {'Name': 'Tats', 'Location': (5, 8), 'Pokemon': [{'Name': 'Bulbasaur', 'HP': 0, 'Max HP': 100},
                                                                     {'Name': 'Charmander', 'HP': 0, 'Max HP': 100},
                                                                     {'Name': 'Squirtle', 'HP': 0, 'Max HP': 100}]}
        event_home(character)
        actual = character['Pokemon']
        expected = [{'Name': 'Bulbasaur', 'HP': 100, 'Max HP': 100},
                    {'Name': 'Charmander', 'HP': 100, 'Max HP': 100},
                    {'Name': 'Squirtle', 'HP': 100, 'Max HP': 100}]
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='')
    def test_print_when_pokemon_are_healed(self, _, mock_output):
        character = {'Name': 'Tats', 'Location': (5, 8), 'Pokemon': [{'Name': 'Bulbasaur', 'HP': 0, 'Max HP': 100},
                                                                     {'Name': 'Charmander', 'HP': 0, 'Max HP': 100},
                                                                     {'Name': 'Squirtle', 'HP': 0, 'Max HP': 100}]}
        event_home(character)
        actual = mock_output.getvalue()
        expected = "Pokémon have been healed!\n"
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='')
    def test_print_when_character_has_no_pokemon(self, _, mock_output):
        character = {'Name': 'Tats', 'Location': (5, 8), 'Pokemon': []}
        event_home(character)
        actual = mock_output.getvalue()
        expected = "Pokémon have been healed!\n"
        self.assertNotIn(expected, actual)
